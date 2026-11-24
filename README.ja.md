# mobile-agent-testers

<a href="https://www.producthunt.com/posts/mobile-agent-testers?utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=mobile-agent-testers"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=dark"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=light" alt="Mobile Agent Testers on Product Hunt" width="250" height="54"></picture></a>
<a href="https://www.linkedin.com/in/pierre-raffalli/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/linkedin-follow-dark.svg"><img src="assets/linkedin-follow-light.svg" alt="Follow Pierre Raffalli on LinkedIn" width="160" height="54"></picture></a>

**本日 [Product Hunt](https://www.producthunt.com/posts/mobile-agent-testers?utm_source=github&utm_medium=readme&utm_campaign=launch-day) でローンチしました。** 役に立ったら、ローンチページでのフィードバックや応援がとても励みになります。

**20 人の AI テスターが、20 台の異なるスマートフォンで、GitHub の無料ランナー上で同時にテスト。**

**[適用例](docs/examples.ja.md)** · **[比較](docs/compare.md)** · **[よくある質問](docs/faq.ja.md)** · **[ペルソナ](personas.json)** · **[コントリビュート](CONTRIBUTING.md)** · **[リリース](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [Español](README.es.md) · [Português](README.pt-BR.md)

<sub>このページは英語版の翻訳です。更新が遅れることがあるため、最新の内容は [README.md](README.md) をご覧ください。</sub>

テストスクリプトを書く必要はありません。各テスターは Claude Code のエージェントで、GitHub Actions 上に
自分専用の iOS シミュレーターまたは Android エミュレーターを持ちます。ペルソナ（スウェーデン語で文字サイズ最大の
iPhone SE、フォント 200% の Pixel 7、ドイツ語の iPad、右から左に読むアラビア語……）を演じ、新しいユーザーとして
アプリを使い（または指定した機能を試し）、スクリーンショット付きのバグレポートを書きます。Flutter、React Native、Expo、ネイティブの Kotlin と
Swift、Kotlin Multiplatform、Capacitor、.NET MAUI に対応しています。

公開リポジトリなら GitHub のランナーは無料です。費用はモデルの利用料だけで、Claude のサブスクリプションか
API キーを使います。[これまでの実行](docs/runs/)では 1 台あたり約 0.15〜0.55 ドルでした。

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="20 人の AI テスターが同時に LocalSend を使う実際の画面録画：Android エミュレーター 10 台と iOS シミュレーター 10 台、14 言語、小さな Pixel から 13 インチの iPad まで。テスターが終わると、その端末に見つけた問題の数が表示されます。クリックで動画を開きます。" width="100%"></a><br>
<sub>LocalSend での実行の実際の画面録画（待ち時間はカット）。<a href="assets/localsend-20.mp4">動画全体（MP4）</a> · <a href="docs/runs/localsend-20.md">端末ごとの実行記録</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## できること

1 回の実行で 1 つの使い方です。設定は[自分のアプリをテストする](#自分のアプリをテストする)の入力で行います。

- **新しいユーザーとして探索**（デフォルト）。各ペルソナが自分の目標を達成しようとし、妨げになったことを番号付きのスクリーンショットとともに報告します。
- **1 つの機能を最初から最後まで試す。** 自分で書いた brief で、各エージェントに 1 つの仕組みを通しで試させます。複数ステップの予約、元に戻せるエディター、2 つの画面間の同期などです。エージェントはタップ、長押し、スワイプ、入力ができ、アプリを離れて戻ったり、再起動して保存内容を確かめたり、ディープリンクで目的の機能から直接始めたりします。brief では約 30 操作という上限を増やすこともできます。[AnkiDroid 用の brief](briefs/ankidroid.md) では、新しいカードの裏面の入力欄がキーボードに隠れることが見つかりました。
- **バグ報告をすべての端末で再現**：issue か手順を渡すと、各エージェントが「再現した / しなかった / はっきりしない」をスクリーンショット付きで答えます（[briefs/reproduce.md](briefs/reproduce.md)）。
- **改善レポートを作る。** 各ペルソナがアプリを一度使い、どこで迷ったか、何を期待していたか、まず何を変えるべきかを、領域と影響度つきで挙げます（[briefs/improve.md](briefs/improve.md)）。
- **2 つのバージョンを比較する。** 同じペルソナで 2 つのブランチやビルドを試し、目標の達成、操作数、スコア、片方のバージョンだけで見つかった問題を 1 つの表にまとめます（[docs/compare-versions.md](docs/compare-versions.md)）。本物の A/B テストの前のチェックであり、その代わりにはなりません。
- **安いモデルを使う**：Claude Haiku、または Anthropic 互換の API（OpenRouter、DeepSeek、Kimi、GLM、MiniMax、Qwen）。見つかるものの質は、モデルがスクリーンショットをどれだけ正しく読めるかと推論力で決まります（[docs/cheaper-models.md](docs/cheaper-models.md)）。

Maestro や Appium はあなたが書いたテストを実行します。このエージェントたちは、誰もテストしようと思わなかったところを探します（[比較](docs/compare.md)）。

## 適用例

オープンソースのアプリでの実際の実行です。仕込んだバグはありません。

| アプリ | 端末 | エージェントが見つけたもの | 時間、モデル使用量 |
|---|---|---|---|
| [LocalSend](https://github.com/localsend/localsend)（Flutter、スター数 10 万） | 20 台：Android 10 台、iOS 10 台、14 言語 | 異なるバグ 46 件、うちブロッカー 1 件：スウェーデン語で文字サイズ最大の iPhone SE では、テキストメッセージを一切送れない | 69 分、4.62 ドル |
| [AnkiDroid](https://github.com/ankidroid/Anki-Android)（Kotlin、スター数 1.2 万、リリース版 APK） | Android 10 台 | 異なる問題 43 件。フォント 200% で回答ボタンが半分に切れる、3 つの言語で「Get started」が英語のまま、など | 10 分未満、4.69 ドル |
| [Flutter 公式のアニメーションサンプル](https://github.com/flutter/packages/tree/main/packages/animations/example) | Android 1 台、iOS 1 台 | 2 つのエージェントがそれぞれ同じタイプミスを報告。アプリはダークモードにも対応していない | 19 分、0.47 ドル |

LocalSend では、46 件のバグのうち 34 件が文字サイズともアクセシビリティとも無関係でした：途中で止まる流れ、黙って失敗する操作、抜けている翻訳、崩れたタブレットのレイアウト。スクリーンショット、すべての指摘、もう一度実行するためのコマンド：[docs/examples.ja.md](docs/examples.ja.md)。

## クイックスタート

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # 鍵ペア + シークレット + Claude トークン（Windows：.\setup.ps1）
gh workflow run agent-testers.yml     # デモ：Android 2 + iOS 2 のテスター、約 20 分
bash scripts/collect.sh <run id>      # レポートを復号して重複をまとめる：runs/<id>/SUMMARY.md
```

デモアプリには[わざと仕込んだバグが 11 個](demo-app/BUGS.md)あります。[ある実行](docs/runs/)では、4 人のデモテスターがそのうち 9 個を見つけ（エージェントごとに 2〜7 分、ビルドを含めて全体で約 21 分）、さらに誰も仕込んでいない本物の問題（Android のナビゲーションバーの下に隠れたボタン、再起動するとデータが残っていない）も見つけました。モデル使用量：4 人で 0.87 ドル。

または、Claude にあなたのアプリ用のセットアップを任せることもできます：

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## 自分のアプリをテストする

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

すべての入力（ビルド、指示書、バグの再現、安いモデル、ビルド引数、動画）と対応フレームワーク：[docs/configuration.ja.md](docs/configuration.ja.md)

## コントリビュート

手伝ってもらえると嬉しいアイデアです。同じものを二人で作らないよう、着手する前に issue でどれをやるか教えてください。それぞれの始め方とオフラインでのテスト方法は [CONTRIBUTING.md](CONTRIBUTING.md) にあります。

- **他のエージェント CLI**：OpenCode、Codex CLI、Gemini CLI、Goose。ツールはただのスクリプトで、ミッションは Markdown の指示書なので、エージェントはプラットフォームごとにコマンド 1 つです。
- **Web アプリ**：Playwright でモバイルブラウザ上に同じペルソナを走らせ、PWA やモバイルサイトを試す。
- **実機の Android**：セルフホストランナーから adb で接続。
- **新しいペルソナ**：コントラストを上げる、視差効果を減らす、色覚フィルター、遅い・不安定なネットワーク。
- **発見を issue に**：サマリーをスクリーンショット付きの GitHub issue の下書きや、Slack・Discord のメッセージにする。
- **他の CI**：GitLab CI、Bitrise、Codemagic。
- **他のビルドシステム**：NativeScript、Unity、Godot。それぞれ `scripts/build/` に case を 1 つ追加。
- **翻訳**：README とドキュメント。
- **モデル比較**：デモアプリに仕込んだ 11 個のバグは小さなベンチマークになります。各モデルが見つけた数とコストの表を。

## チーム向けホスト版（検討中）

このワークフローは今後も無料・オープンソースのまま、機能もすべてそろっています。非公開アプリを持つチーム向けに、ホスト版を検討しています。macOS ランナー込み（非公開リポジトリでは、GitHub は macOS の 1 分を 10 分として数えます）で、レポートをプロダクトマネージャーも含めたチーム全員と共有できる Web ダッシュボード付きです。

チームの役に立ちそうですか？ [3 つの質問に答える](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=teams.yml)か、[LinkedIn で連絡してください](https://www.linkedin.com/in/pierre-raffalli/)。もう自分のアプリで試しましたか？ [見つかったことと、つまずいたところを教えてください](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=usage-feedback.yml)。

## スターの推移

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## クレジット

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

作者：[@pierridotite](https://github.com/pierridotite)（[LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)）· MIT ライセンス
