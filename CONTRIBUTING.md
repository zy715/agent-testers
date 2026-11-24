# Contributing

Thanks for helping. Open an issue before you start, to say what you want to build: two people won't work on the same thing, and we can agree on the shape before you write code. Small pull requests get merged faster than big ones.

## Before you open a pull request

- Run the tests. They are offline and need no phone: `python3 -m unittest discover -s tests -q`.
- Scripts run on GitHub's macOS runners too: keep them working with the bash 3.2 of macOS (no `mapfile`, expand empty arrays as `${ARR[@]+"${ARR[@]}"}`) and with Python 3.9.
- The logs of a public repo are public. Never print a report, a screenshot path with user data, a key or a secret value: print counts and statuses only, like [scripts/build/args.sh](scripts/build/args.sh) and [scripts/agent_status.py](scripts/agent_status.py) do.
- [skills/mobile-agent-testers/SKILL.md](skills/mobile-agent-testers/SKILL.md) and [plugins/mobile-agent-testers/skills/setup/SKILL.md](plugins/mobile-agent-testers/skills/setup/SKILL.md) must stay identical (a test checks it).
- Say how you tested. If you ran it on real emulators or simulators, a link to the run helps.

The README exists in five languages. Change the English one; the translations can follow in the same pull request or a later one.

## Ideas, and where each one starts

### Other agent CLIs (OpenCode, Codex CLI, Gemini CLI, Goose...)

The agent is one command per platform: the `claude -p` call in [scripts/ios/run_agent.sh](scripts/ios/run_agent.sh) and [scripts/android/run_agent.sh](scripts/android/run_agent.sh). Everything else is plain: the tools are scripts (`screen.py`, `gesture.sh` or `adb`, `type.py`) and the mission is a Markdown brief ([AGENT_BRIEF.md](AGENT_BRIEF.md), or a file of [briefs/](briefs/)).

A good shape: an `agent` input in [.github/workflows/agent-testers.yml](.github/workflows/agent-testers.yml) (default: Claude Code), and one sourced script that builds the command for each CLI, next to [scripts/llm_env.sh](scripts/llm_env.sh).

The CLI must be able to run shell commands headless, limited to the tools of the brief (today's allowlist is in `--allowedTools`), read the PNG that `screen.py` writes, write two files under `results/<persona>/`, and stop on its own. [scripts/agent_status.py](scripts/agent_status.py) reads Claude Code's JSON output to say how a run ended: add the new CLI's output there, with tests.

Test it offline with a stand-in for the CLI on `PATH`, like [tests/test_build_args.py](tests/test_build_args.py) does for `flutter`.

### Web apps

The same personas on a mobile browser, for PWAs and mobile sites. A new `web` platform in [scripts/matrix.py](scripts/matrix.py) and [personas.json](personas.json), and `scripts/web/` with the three tools on Playwright: `screen.py` (screenshot plus the list of elements with their centres, in the same format as the phone tools), gestures and typing. It runs on the Linux runners, so it would be the cheapest platform.

### Physical Android phones

On a self-hosted runner with a phone plugged in over USB. [scripts/android/run_agent.sh](scripts/android/run_agent.sh) assumes an emulator: it changes the language with `adb root`, which retail phones refuse, and the workflow starts the emulator with android-emulator-runner. A `device: physical` option would skip both and use the phone that `adb devices` lists.

### New personas

Personas are a few lines in [personas.json](personas.json); the run scripts apply their settings to the phone (text size, dark mode, language and location today). Ideas, asked for by users: increased contrast, reduced motion, color blindness filters, a slow or flaky network.

On Android, these are `adb shell settings put` calls (`secure high_text_contrast_enabled`, the `global` animation scales, `secure accessibility_display_daltonizer`) and the emulator console for the network (`adb emu network speed` and `network delay`). On iOS, check what `xcrun simctl ui` supports in the Xcode of the runner. Add a test in [tests/test_matrix.py](tests/test_matrix.py) for the new fields.

### Findings to issues

[scripts/summarize.py](scripts/summarize.py) writes `SUMMARY.md` on your machine, after [scripts/collect.sh](scripts/collect.sh) decrypts the results. An opt-in step there could open draft issues in your app's repo with `gh issue create`, one per distinct bug, with the personas that hit it and their screenshots, or post the summary to Slack or Discord. It must stay on your machine: the results are private, never upload them from the runner.

### Other CI

The workflow is written for GitHub Actions (job matrix, macOS runners, android-emulator-runner). The build scripts, the persona tools and the encryption ([scripts/encrypt_results.sh](scripts/encrypt_results.sh)) are portable: a GitLab CI, Bitrise or Codemagic version would reuse them.

### More build systems

Framework detection is in [scripts/build/detect.sh](scripts/build/detect.sh), and each framework is one `case` in [scripts/build/android.sh](scripts/build/android.sh) and [scripts/build/ios.sh](scripts/build/ios.sh). NativeScript, Unity or Godot would each be one more case, tested with a stand-in for the build tool.

### Translations

Copy [README.md](README.md) to `README.<language>.md`, keep the headings in the same order, and add the language to the line of languages at the top of every README. The examples page ([docs/examples.md](docs/examples.md)) has translations too.

### Model comparison

The demo app has [11 planted bugs](demo-app/BUGS.md), so it makes a small benchmark. Run the same personas with different models (the `model` and `llm_base_url` inputs, see [docs/cheaper-models.md](docs/cheaper-models.md)) and publish what each one found and cost, as a page of [docs/runs/](docs/runs/) with its JSON data.

## Questions

Open an issue, or a thread in [Discussions](https://github.com/pierridotite/mobile-agent-testers/discussions).
