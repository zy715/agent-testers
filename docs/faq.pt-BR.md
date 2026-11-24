# Perguntas frequentes

[English](faq.md) · [简体中文](faq.zh-CN.md) · [日本語](faq.ja.md) · [Español](faq.es.md) · Português

## 20 agentes não acham o mesmo bug 20 vezes?

Não. No LocalSend, os 103 relatórios eram 46 bugs distintos, e 29 deles foram encontrados por um único agente, incluindo o único bloqueador ([ver a execução](runs/localsend-20.md)). Os bugs de direita para a esquerda só vieram das duas personas em árabe, e os de tablet dos quatro tablets. Os duplicados eram estados do app inteiro que todo mundo encontra, como a lista de aparelhos vazia.

## Quanto custa?

Os runners do GitHub são gratuitos para repositórios públicos, macOS incluído. O uso do modelo foi de US$ 0,15 a US$ 0,55 por agente [nestas execuções](runs/), cerca de US$ 5 para 20 celulares. Com uma assinatura do Claude, as execuções contam no uso do seu plano em vez de virar conta. Para gastar menos, use `model=haiku` ou o modelo de outro provedor: [docs/cheaper-models.md](cheaper-models.md).

## Quanto tempo leva uma execução?

Cada agente explora de 1 a 18 minutos. Os 10 agentes Android do AnkiDroid levaram menos de 10 minutos do início ao último relatório. Os 20 aparelhos do LocalSend levaram 69 minutos, builds incluídos, porque o plano gratuito roda 5 jobs de macOS ao mesmo tempo.

## Preciso de um Mac?

Não. Tudo roda nos runners do GitHub: Linux para Android, macOS para iOS. Você precisa da CLI `gh` e de uma assinatura do Claude ou de uma chave de API, e o `./setup.sh` (`.\setup.ps1` no Windows) faz o resto.

## Duas execuções dão o mesmo resultado?

Não. Cada agente explora, então duas execuções nunca seguem o mesmo caminho: espere os mesmos tipos de bug, não a mesma lista. Mantenha os testes com script (Maestro, Appium) para regressões, veja [a comparação](compare.md).

## Meus relatórios são públicos?

Não. Os logs de um repositório público são públicos, então relatórios, capturas e vídeos são criptografados com a sua chave antes de sair do runner, e só você pode descriptografá-los. Os hosts de analytics são bloqueados dentro dos celulares. Use contas de teste, nunca contas reais. Mais em [PRIVACY.md](../PRIVACY.md).

## Posso testar um app de código fechado?

Sim. Rode o workflow a partir de um repositório privado, com um `SOURCE_REPO_TOKEN` somente leitura para o repositório do seu app, ou faça `android_build` e `ios_build` baixarem um APK ou um .app já compilado. Repositórios privados usam os seus minutos do Actions, e os minutos de macOS contam dez vezes.

## Posso criar minhas próprias personas?

Sim. Uma persona são algumas linhas no [personas.json](../personas.json): aparelho, versão do sistema, idioma, tamanho do texto, modo escuro, localização, quem ela é e o que tenta fazer.

## Onde ele erra?

Às vezes lê uma tela errado: 3 dos 20 agentes do LocalSend apontaram o teclado em inglês do simulador como parte do app. Alguns minutos por agente cobrem os caminhos principais, não cada canto de um app grande. Cada bug relatado vem com capturas numeradas, então confira antes de abrir qualquer issue.

## Limites

- Os runners do GitHub são gratuitos para repositórios públicos: cerca de 20 jobs ao mesmo tempo, 5 no macOS.
- Em planos com limite de uso a cada 5 horas, 20 agentes podem esgotá-lo em ~15 min: rode lotes de 6 a 10.
- Os runners hospedados são feitos para o projeto do próprio repositório. Para um app de código fechado, rode o workflow no seu repositório privado ou no seu próprio Mac.

## Como funciona

<p align="center"><img src="../assets/how-it-works.svg" alt="Como funciona: um workflow faz o build do app, depois um emulador ou simulador com um agente por persona, relatórios criptografados, resumo na sua máquina" width="100%"></p>

- **As personas** definem o aparelho: modelo, sistema, tamanho da fonte, modo escuro, idioma, localização.
- **Três ferramentas por agente**: ver a tela (com coordenadas de toque), gestos, digitação.
- **Verificação de acessibilidade** em cada tela: controles sem nome e áreas de toque menores que 48 dp (Android) ou 44 pt (iOS), que o agente confirma na captura.
- **Resultados criptografados**: os logs de um repositório público são públicos, então tudo é criptografado com a sua chave.
- **Analytics bloqueado** dentro dos celulares, para os testes nunca mexerem nas suas estatísticas reais.
- **Um resumo** na sua máquina: o Claude agrupa os relatórios que descrevem o mesmo bug, então você vê quantas personas encontraram cada um e quais personas encontraram cada tipo de problema.
- **Testes** a cada push, offline e sem celular: verificação de acessibilidade, matriz de personas, resumo, resultados criptografados ([tests/](../tests/)).

## Por que não Maestro, Appium ou agent-device?

Eles rodam os testes que você escreve. Estes agentes procuram o que ninguém pensou em testar.

| | mobile-agent-testers | Maestro, Appium, Detox, e2e |
|---|---|---|
| Você escreve | Nada: escolhe personas da lista | Fluxos ou código de teste |
| Ele pega | Fluxos quebrados, erros silenciosos, textos sem tradução, layout com texto grande, modo escuro, textos confusos | O que cada teste verifica |
| Mesmo resultado a cada execução | Não: cada execução explora, então confira as capturas | Sim |

O [agent-device](https://github.com/callstackincubator/agent-device) dá a um agente de programação o controle de um simulador. Este projeto roda uma sessão inteira: faz o build do app, dá a cada persona seu próprio aparelho e junta relatórios criptografados. Use agentes antes de uma versão e fluxos com script para regressões.

Comparação completa, com Firebase Test Lab Robo, mobile-mcp, phonedriver e beta testers humanos: [docs/compare.md](compare.md) (em inglês).
