# mobile-agent-testers

<a href="https://www.producthunt.com/posts/mobile-agent-testers?utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=mobile-agent-testers"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=dark"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1326513&amp;theme=light" alt="Mobile Agent Testers on Product Hunt" width="250" height="54"></picture></a>
<a href="https://www.linkedin.com/in/pierre-raffalli/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/linkedin-follow-dark.svg"><img src="assets/linkedin-follow-light.svg" alt="Follow Pierre Raffalli on LinkedIn" width="160" height="54"></picture></a>

**Hoy se lanza en [Product Hunt](https://www.producthunt.com/posts/mobile-agent-testers?utm_source=github&utm_medium=readme&utm_campaign=launch-day).** Si te ahorra tiempo, tus comentarios y tu apoyo en la página del lanzamiento ayudan mucho.

**20 testers con IA en 20 teléfonos distintos, en paralelo, en los runners gratuitos de GitHub.**

**[Ejemplos](docs/examples.es.md)** · **[Comparativa](docs/compare.md)** · **[Preguntas frecuentes](docs/faq.es.md)** · **[Personas](personas.json)** · **[Contribuir](CONTRIBUTING.md)** · **[Versiones](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · Español · [Português](README.pt-BR.md)

<sub>Traducción del README en inglés: puede ir con retraso, la referencia es [README.md](README.md).</sub>

Sin scripts de prueba que escribir. Cada tester es un agente de Claude Code con su propio simulador de iOS
o emulador de Android en GitHub Actions. Interpreta una persona (iPhone SE en sueco con el texto más grande,
Pixel 7 al 200 %, iPad en alemán, árabe de derecha a izquierda...), usa tu app como un usuario nuevo (o recorre la función que le indiques) y escribe
un informe de errores con capturas. Flutter, React Native, Expo, Kotlin y Swift nativos, Kotlin
Multiplatform, Capacitor y .NET MAUI.

Los runners de GitHub son gratuitos para repos públicos. Solo pagas el modelo, con tu suscripción de Claude
o tu clave de API: entre 0,15 y 0,55 $ por teléfono en [estas ejecuciones](docs/runs/).

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="Grabaciones de pantalla reales de 20 testers con IA usando LocalSend a la vez: 10 emuladores de Android y 10 simuladores de iOS en 14 idiomas, desde un Pixel pequeño hasta un iPad de 13 pulgadas. Cuando un tester termina, su teléfono muestra cuántos problemas encontró. Abre el vídeo." width="100%"></a><br>
<sub>Grabaciones de pantalla reales de la ejecución en LocalSend, sin los tiempos muertos. <a href="assets/localsend-20.mp4">Vídeo completo (MP4)</a> · <a href="docs/runs/localsend-20.md">La ejecución, dispositivo por dispositivo</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## Qué puede hacer

Un uso por ejecución, elegido con los parámetros de [Prueba tu propia app](#prueba-tu-propia-app).

- **Explorar como usuarios nuevos** (por defecto). Cada persona intenta alcanzar su objetivo y cuenta lo que se lo impide, con capturas numeradas.
- **Recorrer una función de principio a fin.** Tu propio brief manda a cada agente por una mecánica completa: una reserva en varios pasos, un editor con deshacer, una sincronización entre dos pantallas. Los agentes tocan, mantienen pulsado, deslizan y escriben, salen de la app y vuelven, la reinician para comprobar qué se guardó o abren un enlace profundo para empezar directamente en la función, y un brief puede subir el presupuesto de unas 30 acciones. [El de AnkiDroid](briefs/ankidroid.md) encontró el campo del reverso de una tarjeta nueva tapado por el teclado.
- **Reproducir un informe de error** en cada teléfono: das un issue o los pasos, y cada agente responde sí, no o no está claro, con capturas ([briefs/reproduce.md](briefs/reproduce.md)).
- **Obtener un informe de mejoras.** Cada persona usa la app una vez y luego dice dónde dudó, qué esperaba y qué cambiaría primero, por área e impacto ([briefs/improve.md](briefs/improve.md)).
- **Comparar dos versiones.** Las mismas personas en dos ramas o builds, y luego una tabla: objetivos alcanzados, acciones, puntuaciones, errores vistos en una sola versión ([docs/compare-versions.md](docs/compare-versions.md)). Una comprobación antes de un test A/B real, no un sustituto.
- **Usar un modelo más barato**: Claude Haiku, o cualquier API compatible con Anthropic (OpenRouter, DeepSeek, Kimi, GLM, MiniMax, Qwen). Los hallazgos dependen de lo bien que el modelo lea las capturas y razone ([docs/cheaper-models.md](docs/cheaper-models.md)).

Maestro o Appium ejecutan las pruebas que tú escribes. Estos agentes buscan lo que nadie pensó en probar: [comparativa](docs/compare.md).

## Ejemplos aplicados

Ejecuciones reales en apps de código abierto, sin nada plantado.

| App | Teléfonos | Lo que encontraron los agentes | Tiempo, uso del modelo |
|---|---|---|---|
| [LocalSend](https://github.com/localsend/localsend) (Flutter, 100 000 estrellas) | 20: 10 Android, 10 iOS, 14 idiomas | 46 errores distintos, 1 bloqueante: en un iPhone SE en sueco con el texto más grande, no se puede enviar ningún mensaje de texto | 69 min, 4,62 $ |
| [AnkiDroid](https://github.com/ankidroid/Anki-Android) (Kotlin, 12 000 estrellas, APK publicado) | 10 Android | 43 problemas distintos, entre ellos los botones de respuesta cortados por la mitad con la fuente al 200 % y «Get started» en inglés en tres idiomas | menos de 10 min, 4,69 $ |
| [Ejemplo de animaciones de Flutter](https://github.com/flutter/packages/tree/main/packages/animations/example) | 1 Android, 1 iOS | La misma errata, encontrada por los dos agentes cada uno por su cuenta, y una app que ignora el modo oscuro | 19 min, 0,47 $ |

En LocalSend, 34 de los 46 errores no tenían nada que ver con el tamaño del texto ni con la accesibilidad: flujos rotos, fallos silenciosos, traducciones que faltan, diseños de tableta. Capturas, cada hallazgo y los comandos para volver a ejecutarlos: [docs/examples.es.md](docs/examples.es.md).

## Inicio rápido

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # par de claves + secrets + token de Claude (Windows: .\setup.ps1)
gh workflow run agent-testers.yml     # demo: 2 testers Android + 2 iOS, ~20 min
bash scripts/collect.sh <run id>      # descifra los informes y agrupa duplicados: runs/<id>/SUMMARY.md
```

La app de demo tiene [11 errores puestos a propósito](demo-app/BUGS.md). En [una ejecución](docs/runs/), los 4 testers de la demo encontraron 9 (de 2 a 7 minutos por agente, unos 21 minutos en total con las compilaciones), además de problemas reales que nadie había puesto (un botón bajo la barra de navegación de Android, datos que no se guardan al reiniciar). Uso del modelo: 0,87 $ para los 4.

O deja que Claude lo configure para tu app:

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## Prueba tu propia app

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

Todos los parámetros (compilación, briefs, reproducir un bug, modelos más baratos, argumentos de compilación, vídeo) y los frameworks compatibles: [docs/configuration.es.md](docs/configuration.es.md).

## Contribuir

Ideas en las que se agradece ayuda. Abre primero un issue para decir cuál tomas, así dos personas no construyen lo mismo. [CONTRIBUTING.md](CONTRIBUTING.md) explica por dónde empieza cada una y cómo probarla sin conexión.

- **Otros CLI de agentes**: OpenCode, Codex CLI, Gemini CLI, Goose. Las herramientas son scripts normales y la misión es un brief en Markdown, así que el agente es un solo comando por plataforma.
- **Apps web**: las mismas personas en un navegador móvil con Playwright, para PWA y sitios móviles.
- **Teléfonos Android físicos** por adb, en un runner propio.
- **Nuevas personas**: más contraste, menos movimiento, filtros de daltonismo, una red lenta o inestable.
- **De hallazgos a issues**: convertir el resumen en borradores de issues de GitHub con sus capturas, o en un mensaje de Slack o Discord.
- **Otros CI**: GitLab CI, Bitrise, Codemagic.
- **Más sistemas de compilación**: NativeScript, Unity, Godot, cada uno un caso en `scripts/build/`.
- **Traducciones** del README y de la documentación.
- **Comparar modelos**: los 11 bugs plantados en la app de demo forman un pequeño benchmark. Una tabla de lo que encuentra y cuesta cada modelo.

## Versión alojada para equipos (en estudio)

El flujo de este repo sigue siendo gratis, de código abierto y completo. Estoy estudiando una versión alojada para equipos con apps privadas: runners de macOS incluidos (en un repo privado, GitHub cuenta cada minuto de macOS diez veces) y un panel web para compartir los informes con todo el equipo, product managers incluidos.

¿Le serviría a tu equipo? [Responde tres preguntas](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=teams.yml) o [escríbeme por LinkedIn](https://www.linkedin.com/in/pierre-raffalli/). ¿Ya lo probaste con tu app? [Cuéntame qué encontró y qué te frenó](https://github.com/pierridotite/mobile-agent-testers/issues/new?template=usage-feedback.yml).

## Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## Créditos

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

Hecho por [@pierridotite](https://github.com/pierridotite) ([LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)) · licencia MIT
