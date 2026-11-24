# 自分のアプリをテストする

[English](configuration.md) · [简体中文](configuration.zh-CN.md) · 日本語 · [Español](configuration.es.md) · [Português](configuration.pt-BR.md)

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| 入力 | |
|---|---|
| `source_repo`, `ref` | アプリのリポジトリとブランチ（空 = このリポジトリ）。プライベートリポジトリの場合は読み取り専用の `SOURCE_REPO_TOKEN` シークレットを追加 |
| `app_dir`, `app_id` | アプリのフォルダー、Android のパッケージ名 / iOS の bundle id（もう一方のプラットフォームが別の id を使う場合は、ビルドしたアプリから読み取ります） |
| `android_personas`, `ios_personas` | [personas.json](../personas.json) の id（1 つにつき 1 台）、`all`、またはプラットフォームを飛ばす `none`。20 人が用意済み：14 言語、右から左、タブレット、小さい文字からアクセシビリティの最大サイズまで |
| `brief` | エージェントへの指示：探索なら [AGENT_BRIEF.md](../AGENT_BRIEF.md)、改善レポートなら [briefs/improve.md](../briefs/improve.md)、1 つの機能を試すなら自分で書いたもの |
| `bug_report` | 探索の代わりに再現するバグ：issue（`owner/repo#123` またはその URL）か、手順をそのまま書いたテキスト。各エージェントが自分の端末でその手順を試します（[briefs/reproduce.md](../briefs/reproduce.md)） |
| `model`、`llm_base_url` | デフォルトは `sonnet`。費用を抑えるなら `haiku`、または Anthropic 互換の任意の API（キーは `LLM_API_KEY` シークレットに設定）（[docs/cheaper-models.md](cheaper-models.md)） |
| `framework` | `auto`（デフォルト）、または下のフレームワークのいずれかを指定 |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | 独自のビルドコマンド、またはビルド済みアプリのダウンロード（パスは `app_dir` からの相対パス） |
| `build_args` | 自動ビルドに追加する引数（両プラットフォーム共通）。Flutter なら `--dart-define=API_URL=https://staging.example.com`、それ以外は Gradle と xcodebuild の引数。公開リポジトリでは実行時の入力も公開されるので、キーは `BUILD_ARGS` シークレットに入れてください |
| `block_hosts` | テスト中にブロックする分析系のホスト |
| `record_video` | 各端末の画面録画（レポートと一緒に暗号化） |

**そのまま使えるもの**（自動検出）：

| フレームワーク | Android | iOS シミュレーター |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| ネイティブ Kotlin / Java、Swift / Objective-C | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | iOS アプリの Xcode プロジェクト |
| Capacitor / Ionic | `cap sync` 後に Gradle debug | `cap sync` 後に Xcode |
| .NET MAUI（ベータ） | `dotnet publish` | `iossimulator-arm64` 向けの `dotnet build` |
| その他すべて | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

エージェントはスクリーンショットとアクセシビリティツリーから画面を読むので、どの UI ツールキットでも動きます。ラベル付きのウィジェット（Flutter の `Semantics`、`contentDescription`、`accessibilityLabel`）があると、より正確にタップできます。
