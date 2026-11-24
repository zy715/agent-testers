# mobile-agent-testers

<a href="https://www.producthunt.com/posts/mobile-agent-testers?utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=mobile-agent-testers"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=dark"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=light" alt="Mobile Agent Testers on Product Hunt" width="250" height="54"></picture></a>
<a href="https://www.linkedin.com/in/pierre-raffalli/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/linkedin-follow-dark.svg"><img src="assets/linkedin-follow-light.svg" alt="Follow Pierre Raffalli on LinkedIn" width="160" height="54"></picture></a>

**今天在 [Product Hunt](https://www.producthunt.com/posts/mobile-agent-testers?utm_source=github&utm_medium=readme&utm_campaign=launch-day) 上线。** 如果它帮你省了时间，欢迎到发布页留下反馈、支持一下。

**20 个 AI 测试员，20 台不同的手机，在 GitHub 的免费运行器上并行测试。**

**[应用实例](docs/examples.zh-CN.md)** · **[对比](docs/compare.md)** · **[常见问题](docs/faq.zh-CN.md)** · **[角色](personas.json)** · **[参与贡献](CONTRIBUTING.md)** · **[版本](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · 简体中文 · [日本語](README.ja.md) · [Español](README.es.md) · [Português](README.pt-BR.md)

<sub>本页译自英文版，可能稍有滞后，以 [README.md](README.md) 为准。</sub>

无需编写测试脚本。每个测试员都是一个 Claude Code 智能体，在 GitHub Actions 上拥有自己的 iOS
模拟器或 Android 模拟器。它扮演一个角色（瑞典语、最大字号的 iPhone SE，字体 200% 的 Pixel 7，
德语 iPad，从右到左的阿拉伯语……），像新用户一样使用你的应用（或者按你的要求测某个功能），并写出带截图的缺陷报告。
支持 Flutter、React Native、Expo、原生 Kotlin 和 Swift、Kotlin Multiplatform、Capacitor 和 .NET MAUI。

公开仓库使用 GitHub 的运行器是免费的。你只需要为模型付费，用你的 Claude 订阅或 API key：
在[这几次运行](docs/runs/)中，每台手机大约 0.15 到 0.55 美元。

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="20 个 AI 测试员同时使用 LocalSend 的真实录屏：10 台 Android 模拟器和 10 台 iOS 模拟器，14 种语言，从小屏 Pixel 到 13 英寸 iPad。测试员完成后，手机上会显示它发现的问题数量。点击打开视频。" width="100%"></a><br>
<sub>LocalSend 那次运行的真实录屏，已剪掉空闲时间。<a href="assets/localsend-20.mp4">完整视频（MP4）</a> · <a href="docs/runs/localsend-20.md">逐台设备查看这次运行</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## 能做什么

每次运行一种用法，用[测试你自己的应用](#测试你自己的应用)里的参数来设置。

- **像新用户一样探索**（默认）。每个角色都会努力完成自己的目标，并报告一路上遇到的障碍，附带编号截图。
- **把一个功能从头测到尾。** 用你自己的 brief 让每个智能体完整走一遍某个机制：分几步的预订、带撤销的编辑器、两个页面之间的同步。智能体会点按、长按、滑动和输入，离开应用再回来，重启应用检查保存了什么，或者打开深层链接直接进入这个功能；brief 还可以提高默认约 30 步操作的预算。[AnkiDroid 的 brief](briefs/ankidroid.md) 就发现新卡片的背面输入框被键盘挡住了。
- **在每台手机上复现一个缺陷报告**：给出一个 issue 或复现步骤，每个智能体回答“是 / 否 / 不确定”，并附上截图（[briefs/reproduce.md](briefs/reproduce.md)）。
- **生成改进报告。** 每个角色把应用用一遍，然后说出在哪里犹豫、原本期待什么、最该先改什么，并标出领域和影响（[briefs/improve.md](briefs/improve.md)）。
- **对比两个版本。** 同一批角色分别使用两个分支或构建，最后得到一张表：目标是否达成、操作次数、评分、只在一个版本出现的问题（[docs/compare-versions.md](docs/compare-versions.md)）。适合在真正的 A/B 测试之前做检查，但不能代替 A/B 测试。
- **使用更便宜的模型**：Claude Haiku，或任何兼容 Anthropic 接口的 API（OpenRouter、DeepSeek、Kimi、GLM、MiniMax、通义千问）。发现的质量取决于模型读截图的能力和推理能力（[docs/cheaper-models.md](docs/cheaper-models.md)）。

Maestro、Appium 运行你写好的测试。这些智能体寻找没人想到要测的东西：[对比](docs/compare.md)。

## 应用实例

在开源应用上的真实运行，没有预先埋入任何缺陷。

| 应用 | 手机 | 智能体发现了什么 | 用时、模型用量 |
|---|---|---|---|
| [LocalSend](https://github.com/localsend/localsend)（Flutter，10 万星） | 20 台：10 台 Android、10 台 iOS，14 种语言 | 46 个不同的缺陷，其中 1 个阻断级：瑞典语、最大字号的 iPhone SE 上根本无法发送文字消息 | 69 分钟，4.62 美元 |
| [AnkiDroid](https://github.com/ankidroid/Anki-Android)（Kotlin，1.2 万星，发布版 APK） | 10 台 Android | 43 个不同的问题，比如字体 200% 时答题按钮被切掉一半，三种语言里“Get started”仍是英文 | 不到 10 分钟，4.69 美元 |
| [Flutter 官方动画示例](https://github.com/flutter/packages/tree/main/packages/animations/example) | 1 台 Android、1 台 iOS | 两个智能体各自报告了同一个拼写错误，还发现应用不支持深色模式 | 19 分钟，0.47 美元 |

在 LocalSend 上，46 个缺陷中有 34 个与字号和无障碍都无关：流程中断、静默失败、缺失的翻译、平板布局。截图、每个发现以及重新运行的命令：[docs/examples.zh-CN.md](docs/examples.zh-CN.md)。

## 快速开始

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # 密钥对 + secrets + Claude 令牌（Windows：.\setup.ps1）
gh workflow run agent-testers.yml     # 演示：2 个 Android + 2 个 iOS 测试员，约 20 分钟
bash scripts/collect.sh <run id>      # 解密报告并归并重复项：runs/<id>/SUMMARY.md
```

演示应用里有 [11 个故意埋下的缺陷](demo-app/BUGS.md)。在[一次运行](docs/runs/)中，4 个演示测试员找到了其中 9 个（每个智能体 2 到 7 分钟，整次运行约 21 分钟，含构建），还发现了没人埋下的真实问题（一个按钮被 Android 导航栏挡住、重新启动后数据没有保留）。模型用量：4 个共 0.87 美元。

或者让 Claude 为你的应用完成设置：

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## 测试你自己的应用

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

全部参数（构建、任务说明、复现 bug、更便宜的模型、构建参数、录屏）和支持的框架：[docs/configuration.zh-CN.md](docs/configuration.zh-CN.md)

## 参与贡献

以下方向欢迎帮忙。动手前先开一个 issue 说明你要做哪一项，避免两个人做同一件事。[CONTRIBUTING.md](CONTRIBUTING.md) 写明了每一项从哪里入手，以及如何离线测试。

- **其他智能体 CLI**：OpenCode、Codex CLI、Gemini CLI、Goose。工具都是普通脚本，任务是一份 Markdown 说明，所以每个平台只需换一条命令。
- **Web 应用**：用 Playwright 在手机浏览器里跑同样的角色，覆盖 PWA 和移动网站。
- **真实 Android 手机**：在自托管 runner 上通过 adb 连接。
- **新角色**：增强对比度、减弱动态效果、色盲滤镜、慢速或不稳定的网络。
- **把发现变成 issue**：把汇总转成带截图的 GitHub issue 草稿，或发到 Slack、Discord。
- **其他 CI**：GitLab CI、Bitrise、Codemagic。
- **更多构建系统**：NativeScript、Unity、Godot，每种在 `scripts/build/` 里加一个分支。
- **翻译** README 和文档。
- **模型对比**：演示应用里预埋的 11 个 bug 就是一个小基准。做一张表，列出每个模型找到多少、花多少钱。

## 团队托管版（探索中）

这里的工作流会一直免费、开源、完整。我正在探索一个面向私有应用团队的托管版：包含 macOS 运行器（在私有仓库里，GitHub 把 macOS 的每一分钟按十分钟计算），以及一个网页面板，方便把报告分享给整个团队，包括产品经理。

对你的团队有用吗？[回答三个问题](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=teams.yml)，或[在 LinkedIn 上联系我](https://www.linkedin.com/in/pierre-raffalli/)。已经在你的应用上跑过了？[告诉我它发现了什么、哪里卡住了](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=usage-feedback.yml)。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## 致谢

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

由 [@pierridotite](https://github.com/pierridotite) 制作（[LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)）· MIT 许可证
