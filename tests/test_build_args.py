"""build_args input and BUILD_ARGS secret, offline: scripts/build/args.sh, then the
automatic Flutter builds of both platforms with a stand-in for flutter."""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAKE_FLUTTER = """#!/usr/bin/env bash
printf '%s\\n' "$@" > "$FAKE_LOG.$1.$2"
case "$1 $2" in
  "build apk") mkdir -p build/app/outputs/flutter-apk && echo apk > build/app/outputs/flutter-apk/app-debug.apk ;;
  "build ios") mkdir -p build/ios/iphonesimulator/Runner.app ;;
esac
"""


def parse(build_args="", secret=""):
    script = ('set -u; . scripts/build/args.sh; build_args; code=$?; '
              'echo "code=$code"; for a in ${BUILD_ARGV[@]+"${BUILD_ARGV[@]}"}; do echo "arg=$a"; done')
    env = dict(os.environ, BUILD_ARGS=build_args, BUILD_ARGS_SECRET=secret)
    out = subprocess.run(["bash", "-c", script], cwd=ROOT, env=env, capture_output=True, text=True).stdout
    args = [l[4:] for l in out.splitlines() if l.startswith("arg=")]
    shown = "\n".join(l for l in out.splitlines() if not l.startswith("arg="))
    return args, shown


class Parse(unittest.TestCase):
    def test_input_then_secret_with_shell_quotes(self):
        args, shown = parse('--dart-define=API_URL=https://staging.example.com --dart-define="TITLE=two words"',
                            "--dart-define=KEY=s3cret")
        self.assertEqual(args, ["--dart-define=API_URL=https://staging.example.com",
                                "--dart-define=TITLE=two words", "--dart-define=KEY=s3cret"])
        self.assertIn("Extra build arguments: 3", shown)
        self.assertIn("code=0", shown)
        self.assertNotIn("s3cret", shown)

    def test_nothing_set_is_fine_under_set_u(self):
        args, shown = parse("", "  ")
        self.assertEqual(args, [])
        self.assertIn("code=0", shown)
        self.assertNotIn("Extra build arguments", shown)

    def test_unbalanced_quotes_fail_without_showing_values(self):
        args, shown = parse("", '--dart-define="KEY=s3cret')
        self.assertIn("code=1", shown)
        self.assertIn("unbalanced quotes", shown)
        self.assertNotIn("s3cret", shown)


class FlutterBuilds(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        shutil.copytree(ROOT / "scripts" / "build", self.root / "scripts" / "build")
        (self.root / "app").mkdir()
        (self.root / "app" / "pubspec.yaml").write_text("name: app\n")
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        (bin_dir / "flutter").write_text(FAKE_FLUTTER)
        (bin_dir / "flutter").chmod(0o755)
        self.log = self.root / "flutter-args"
        self.env = dict(os.environ, PATH=f"{bin_dir}:{os.environ['PATH']}", GITHUB_WORKSPACE=str(self.root),
                        RUNNER_TEMP=str(self.root / "tmp"), FAKE_LOG=str(self.log),
                        BUILD_ARGS="--dart-define=API_URL=https://staging.example.com",
                        BUILD_ARGS_SECRET="--dart-define=KEY=s3cret")

    def build(self, platform, **env):
        return subprocess.run(["bash", f"scripts/build/{platform}.sh", "app", "auto"], cwd=self.root,
                              env=dict(self.env, **env), capture_output=True, text=True)

    def test_android(self):
        proc = self.build("android")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        args = Path(f"{self.log}.build.apk").read_text().split("\n")
        self.assertIn("--dart-define=API_URL=https://staging.example.com", args)
        self.assertIn("--dart-define=KEY=s3cret", args)
        self.assertTrue((self.root / "app.apk").exists())
        self.assertNotIn("s3cret", proc.stdout + proc.stderr)

    def test_ios(self):
        proc = self.build("ios")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        args = Path(f"{self.log}.build.ios").read_text().split("\n")
        self.assertEqual(args[:3], ["build", "ios", "--simulator"])
        self.assertIn("--dart-define=KEY=s3cret", args)
        self.assertTrue((self.root / "app-ios.tgz").exists())

    def test_no_extra_arguments(self):
        proc = self.build("android", BUILD_ARGS="", BUILD_ARGS_SECRET="")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        args = [a for a in Path(f"{self.log}.build.apk").read_text().split("\n") if a]
        self.assertEqual(args, ["build", "apk", "--debug", "--target-platform", "android-x64"])

    def test_ignored_with_a_custom_build_command(self):
        (self.root / "app" / "prebuilt.apk").write_text("apk")
        proc = self.build("android", BUILD_COMMAND="true", ARTIFACT="prebuilt.apk")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("::warning::build_args is ignored with a custom android_build command", proc.stdout)


if __name__ == "__main__":
    unittest.main()
