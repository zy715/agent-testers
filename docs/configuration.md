# Test your own app

English · [简体中文](configuration.zh-CN.md) · [日本語](configuration.ja.md) · [Español](configuration.es.md) · [Português](configuration.pt-BR.md)

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| Input | |
|---|---|
| `source_repo`, `ref` | App repo and branch (empty = this repo). Private repo: add a read-only `SOURCE_REPO_TOKEN` secret |
| `app_dir`, `app_id` | App folder, Android package / iOS bundle id (if the other platform uses another id, it is read from its built app) |
| `android_personas`, `ios_personas` | Ids from [personas.json](../personas.json), one phone each, `all`, or `none` to skip a platform. 20 ready: 14 languages, right to left, tablets, text from small to the largest accessibility size |
| `brief` | Agent instructions: [AGENT_BRIEF.md](../AGENT_BRIEF.md) to explore, [briefs/improve.md](../briefs/improve.md) for an improvement report, or your own for one feature |
| `bug_report` | A bug to reproduce instead of exploring: an issue (`owner/repo#123` or its URL) or the steps as text. Each agent follows it on its own device ([briefs/reproduce.md](../briefs/reproduce.md)) |
| `model`, `llm_base_url` | `sonnet` by default, `haiku` to spend less, or any Anthropic-compatible API with its key in an `LLM_API_KEY` secret ([docs/cheaper-models.md](cheaper-models.md)) |
| `framework` | `auto` (default) or force one of the frameworks below |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | Your own build command, or a download of a prebuilt app (paths relative to `app_dir`) |
| `build_args` | Extra arguments for the automatic build of both platforms, like `--dart-define=API_URL=https://staging.example.com` for Flutter (Gradle and xcodebuild arguments for the others). Keys go in a `BUILD_ARGS` secret: run inputs are public on a public repo |
| `block_hosts` | Analytics hosts blocked during tests |
| `record_video` | Screen recording of each phone, encrypted with the reports |

**Supported out of the box** (detected automatically):

| Framework | Android | iOS Simulator |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| Native Kotlin / Java, Swift / Objective-C | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | Xcode project of the iOS app |
| Capacitor / Ionic | Gradle debug after `cap sync` | Xcode after `cap sync` |
| .NET MAUI (beta) | `dotnet publish` | `dotnet build` for `iossimulator-arm64` |
| Anything else | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

Agents read the screen from screenshots and the accessibility tree, so any UI
toolkit works. Labelled widgets (Flutter `Semantics`, `contentDescription`,
`accessibilityLabel`) give them more precise tap targets.
