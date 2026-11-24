# 测试你自己的应用

[English](configuration.md) · 简体中文 · [日本語](configuration.ja.md) · [Español](configuration.es.md) · [Português](configuration.pt-BR.md)

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| 输入 | |
|---|---|
| `source_repo`, `ref` | 应用仓库和分支（留空 = 本仓库）。私有仓库：添加一个只读的 `SOURCE_REPO_TOKEN` secret |
| `app_dir`, `app_id` | 应用目录，Android 包名 / iOS bundle id（如果另一个平台用的是别的 id，会从它的构建产物中读取） |
| `android_personas`, `ios_personas` | [personas.json](../personas.json) 中的 id，每个角色一台手机；`all` 表示全部，`none` 表示跳过该平台。内置 20 个角色：14 种语言、从右到左、平板、从小号到最大辅助功能字号 |
| `brief` | 给智能体的说明：[AGENT_BRIEF.md](../AGENT_BRIEF.md) 用于探索，[briefs/improve.md](../briefs/improve.md) 用于改进报告，也可以用你自己写的来测某个功能 |
| `bug_report` | 要复现的缺陷，而不是自由探索：一个 issue（`owner/repo#123` 或它的链接），或者直接写步骤。每个智能体在自己的设备上照着做（[briefs/reproduce.md](../briefs/reproduce.md)） |
| `model`、`llm_base_url` | 默认 `sonnet`，想省钱用 `haiku`，也可以用任何兼容 Anthropic 接口的 API，密钥放在 `LLM_API_KEY` secret 里（[docs/cheaper-models.md](cheaper-models.md)） |
| `framework` | `auto`（默认），或强制使用下表中的某个框架 |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | 你自己的构建命令，或下载一个预构建的应用（路径相对于 `app_dir`） |
| `build_args` | 自动构建时追加的参数，两个平台都生效：Flutter 用 `--dart-define=API_URL=https://staging.example.com`，其他框架是 Gradle 和 xcodebuild 的参数。公开仓库里每次运行的输入都是公开的，密钥请放进 `BUILD_ARGS` secret |
| `block_hosts` | 测试期间屏蔽的统计分析域名 |
| `record_video` | 每台手机的录屏，与报告一起加密 |

**开箱即用**（自动检测）：

| 框架 | Android | iOS 模拟器 |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| 原生 Kotlin / Java、Swift / Objective-C | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | iOS 应用的 Xcode 工程 |
| Capacitor / Ionic | `cap sync` 后 Gradle debug | `cap sync` 后 Xcode |
| .NET MAUI（测试版） | `dotnet publish` | 针对 `iossimulator-arm64` 的 `dotnet build` |
| 其他任何框架 | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

智能体通过截图和无障碍树读取屏幕，所以任何 UI 工具包都适用。带标签的控件（Flutter `Semantics`、`contentDescription`、`accessibilityLabel`）能让它们点得更准。
