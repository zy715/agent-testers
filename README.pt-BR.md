# mobile-agent-testers

<a href="https://www.producthunt.com/posts/mobile-agent-testers?utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=mobile-agent-testers"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=dark"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=light" alt="Mobile Agent Testers on Product Hunt" width="250" height="54"></picture></a>
<a href="https://www.linkedin.com/in/pierre-raffalli/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/linkedin-follow-dark.svg"><img src="assets/linkedin-follow-light.svg" alt="Follow Pierre Raffalli on LinkedIn" width="160" height="54"></picture></a>

**Lançamento no [Product Hunt](https://www.producthunt.com/posts/mobile-agent-testers?utm_source=github&utm_medium=readme&utm_campaign=launch-day) hoje.** Se ele te poupa tempo, seu feedback e seu apoio na página do lançamento ajudam muito.

**20 testadores com IA em 20 celulares diferentes, em paralelo, nos runners gratuitos do GitHub.**

**[Exemplos](docs/examples.pt-BR.md)** · **[Comparação](docs/compare.md)** · **[Perguntas frequentes](docs/faq.pt-BR.md)** · **[Personas](personas.json)** · **[Contribuir](CONTRIBUTING.md)** · **[Versões](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · Português

<sub>Tradução do README em inglês: pode estar atrasada, a referência é o [README.md](README.md).</sub>

Nenhum script de teste para escrever. Cada testador é um agente do Claude Code com seu próprio simulador de iOS
ou emulador de Android no GitHub Actions. Ele interpreta uma persona (iPhone SE em sueco com o maior tamanho de
texto, Pixel 7 a 200%, iPad em alemão, árabe da direita para a esquerda...), usa o seu app como um usuário novo (ou percorre a função que você indicar) e
escreve um relatório de bugs com capturas de tela. Flutter, React Native, Expo, Kotlin e Swift nativos, Kotlin
Multiplatform, Capacitor e .NET MAUI.

Os runners do GitHub são gratuitos para repositórios públicos. Você paga só o modelo, com sua assinatura do
Claude ou chave de API: de US$ 0,15 a US$ 0,55 por celular [nestas execuções](docs/runs/).

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="Gravações de tela reais de 20 testadores com IA usando o LocalSend ao mesmo tempo: 10 emuladores de Android e 10 simuladores de iOS em 14 idiomas, de um Pixel pequeno a um iPad de 13 polegadas. Quando um testador termina, o celular mostra quantos problemas ele encontrou. Abre o vídeo." width="100%"></a><br>
<sub>Gravações de tela reais da execução no LocalSend, sem os tempos de espera. <a href="assets/localsend-20.mp4">Vídeo completo (MP4)</a> · <a href="docs/runs/localsend-20.md">A execução, aparelho por aparelho</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## O que ele faz

Um uso por execução, escolhido com os parâmetros de [Teste o seu próprio app](#teste-o-seu-próprio-app).

- **Explorar como usuários novos** (o padrão). Cada persona tenta chegar ao seu objetivo e conta o que atrapalha, com capturas numeradas.
- **Percorrer uma função do começo ao fim.** O seu próprio brief manda cada agente por uma mecânica inteira: uma reserva em várias etapas, um editor com desfazer, uma sincronização entre duas telas. Os agentes tocam, pressionam e seguram, deslizam e digitam, saem do app e voltam, reiniciam o app para conferir o que foi salvo ou abrem um deep link para começar direto na função, e um brief pode aumentar o orçamento de cerca de 30 ações. [O do AnkiDroid](briefs/ankidroid.md) encontrou o campo do verso de um cartão novo escondido atrás do teclado.
- **Reproduzir um relato de bug** em cada celular: você passa uma issue ou os passos, e cada agente responde sim, não ou incerto, com capturas ([briefs/reproduce.md](briefs/reproduce.md)).
- **Gerar um relatório de melhorias.** Cada persona usa o app uma vez e depois diz onde hesitou, o que esperava e o que mudaria primeiro, por área e impacto ([briefs/improve.md](briefs/improve.md)).
- **Comparar duas versões.** As mesmas personas em dois branches ou builds, e depois uma tabela: objetivos alcançados, ações, notas, problemas vistos em uma versão só ([docs/compare-versions.md](docs/compare-versions.md)). Uma checagem antes de um teste A/B de verdade, não um substituto.
- **Usar um modelo mais barato**: Claude Haiku, ou qualquer API compatível com a Anthropic (OpenRouter, DeepSeek, Kimi, GLM, MiniMax, Qwen). Os achados dependem de quão bem o modelo lê as capturas e raciocina ([docs/cheaper-models.md](docs/cheaper-models.md)).

Maestro ou Appium rodam os testes que você escreve. Estes agentes procuram o que ninguém pensou em testar: [comparação](docs/compare.md).

## Exemplos aplicados

Execuções reais em apps de código aberto, sem nada plantado.

| App | Celulares | O que os agentes encontraram | Tempo, uso do modelo |
|---|---|---|---|
| [LocalSend](https://github.com/localsend/localsend) (Flutter, 100 mil estrelas) | 20: 10 Android, 10 iOS, 14 idiomas | 46 bugs distintos, 1 bloqueador: num iPhone SE em sueco com o maior tamanho de texto, não dá para enviar nenhuma mensagem de texto | 69 min, US$ 4,62 |
| [AnkiDroid](https://github.com/ankidroid/Anki-Android) (Kotlin, 12 mil estrelas, APK publicado) | 10 Android | 43 problemas distintos, entre eles os botões de resposta cortados pela metade com a fonte a 200% e "Get started" em inglês em três idiomas | menos de 10 min, US$ 4,69 |
| [Exemplo de animações do Flutter](https://github.com/flutter/packages/tree/main/packages/animations/example) | 1 Android, 1 iOS | O mesmo erro de digitação, encontrado pelos dois agentes, cada um por conta própria, e um app que ignora o modo escuro | 19 min, US$ 0,47 |

No LocalSend, 34 dos 46 bugs não tinham nada a ver com tamanho de texto nem com acessibilidade: fluxos quebrados, falhas silenciosas, traduções faltando, layouts de tablet. Capturas de tela, cada bug encontrado e os comandos para rodar de novo: [docs/examples.pt-BR.md](docs/examples.pt-BR.md).

## Começo rápido

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # par de chaves + secrets + token do Claude (Windows: .\setup.ps1)
gh workflow run agent-testers.yml     # demo: 2 testadores Android + 2 iOS, ~20 min
bash scripts/collect.sh <run id>      # descriptografa os relatórios e agrupa duplicados: runs/<id>/SUMMARY.md
```

O app de demo tem [11 bugs colocados de propósito](demo-app/BUGS.md). Em [uma execução](docs/runs/), os 4 testadores da demo encontraram 9 deles (de 2 a 7 minutos por agente, cerca de 21 minutos no total, builds incluídos), além de problemas reais que ninguém colocou (um botão debaixo da barra de navegação do Android, dados que não ficam salvos depois de reabrir). Uso do modelo: US$ 0,87 para os 4.

Ou deixe o Claude configurar para o seu app:

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## Teste o seu próprio app

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

Todos os parâmetros (build, briefs, reproduzir um bug, modelos mais baratos, argumentos de build, vídeo) e os frameworks suportados: [docs/configuration.pt-BR.md](docs/configuration.pt-BR.md).

## Contribuir

Ideias em que ajuda é bem-vinda. Abra uma issue antes para dizer qual você vai pegar, assim duas pessoas não constroem a mesma coisa. O [CONTRIBUTING.md](CONTRIBUTING.md) diz por onde cada uma começa e como testar offline.

- **Outros CLIs de agente**: OpenCode, Codex CLI, Gemini CLI, Goose. As ferramentas são scripts comuns e a missão é um brief em Markdown, então o agente é um único comando por plataforma.
- **Apps web**: as mesmas personas num navegador mobile com Playwright, para PWAs e sites mobile.
- **Celulares Android físicos** via adb, num runner próprio.
- **Novas personas**: mais contraste, menos movimento, filtros de daltonismo, rede lenta ou instável.
- **Achados viram issues**: transformar o resumo em rascunhos de issues do GitHub com as capturas, ou numa mensagem no Slack ou Discord.
- **Outros CIs**: GitLab CI, Bitrise, Codemagic.
- **Mais sistemas de build**: NativeScript, Unity, Godot, cada um um caso em `scripts/build/`.
- **Traduções** do README e da documentação.
- **Comparar modelos**: os 11 bugs plantados no app de demonstração formam um pequeno benchmark. Uma tabela do que cada modelo encontra e quanto custa.

## Versão hospedada para equipes (em estudo)

O fluxo deste repositório continua gratuito, de código aberto e completo. Estou estudando uma versão hospedada para equipes com apps privados: runners macOS incluídos (num repositório privado, o GitHub conta cada minuto de macOS dez vezes) e um painel web para compartilhar os relatórios com a equipe toda, product managers incluídos.

Isso ajudaria a sua equipe? [Responda três perguntas](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=teams.yml) ou [fale comigo no LinkedIn](https://www.linkedin.com/in/pierre-raffalli/). Já rodou no seu app? [Conte o que ele encontrou e o que atrapalhou](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=usage-feedback.yml).

## Histórico de estrelas

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## Créditos

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

Feito por [@pierridotite](https://github.com/pierridotite) ([LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)) · licença MIT
