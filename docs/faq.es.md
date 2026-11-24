# Preguntas frecuentes

[English](faq.md) · [简体中文](faq.zh-CN.md) · [日本語](faq.ja.md) · Español · [Português](faq.pt-BR.md)

## ¿20 agentes no encuentran 20 veces el mismo error?

No. En LocalSend, los 103 informes eran 46 errores distintos, y 29 de ellos los encontró un solo agente, incluido el único bloqueante ([ver la ejecución](runs/localsend-20.md)). Los errores de derecha a izquierda solo vinieron de las dos personas en árabe, y los de tableta de las cuatro tabletas. Los duplicados eran estados de toda la app con los que todos se cruzan, como la lista de dispositivos vacía.

## ¿Cuánto cuesta?

Los runners de GitHub son gratis para repositorios públicos, macOS incluido. El uso del modelo fue de 0,15 a 0,55 $ por agente en [estas ejecuciones](runs/), unos 5 $ para 20 teléfonos. Con una suscripción a Claude, las ejecuciones cuentan en el uso de tu plan en lugar de facturarse. Para gastar menos, usa `model=haiku` o el modelo de otro proveedor: [docs/cheaper-models.md](cheaper-models.md).

## ¿Cuánto tarda una ejecución?

Cada agente explora de 1 a 18 minutos. Los 10 agentes Android de AnkiDroid tardaron menos de 10 minutos desde el inicio hasta el último informe. Los 20 dispositivos de LocalSend tardaron 69 minutos, compilaciones incluidas, porque el plan gratuito ejecuta 5 trabajos de macOS a la vez.

## ¿Necesito un Mac?

No. Todo se ejecuta en los runners de GitHub: Linux para Android, macOS para iOS. Necesitas la CLI `gh` y una suscripción a Claude o una clave de API, y `./setup.sh` (`.\setup.ps1` en Windows) hace el resto.

## ¿Dos ejecuciones dan el mismo resultado?

No. Cada agente explora, así que dos ejecuciones nunca siguen el mismo camino: espera los mismos tipos de errores, no la misma lista. Mantén las pruebas con script (Maestro, Appium) para las regresiones, mira [la comparativa](compare.md).

## ¿Mis informes son públicos?

No. Los logs de un repositorio público son públicos, así que los informes, las capturas y los vídeos se cifran con tu clave antes de salir del runner, y solo tú puedes descifrarlos. Los hosts de analítica se bloquean dentro de los teléfonos. Usa cuentas de prueba, nunca reales. Más en [PRIVACY.md](../PRIVACY.md).

## ¿Puedo probar una app de código cerrado?

Sí. Ejecuta el workflow desde un repositorio privado, con un `SOURCE_REPO_TOKEN` de solo lectura para el repositorio de tu app, o haz que `android_build` e `ios_build` descarguen un APK o un .app ya compilados. Los repositorios privados consumen tus minutos de Actions, y los minutos de macOS cuentan diez veces.

## ¿Puedo crear mis propias personas?

Sí. Una persona son unas pocas líneas en [personas.json](../personas.json): dispositivo, versión del sistema, idioma, tamaño de texto, modo oscuro, ubicación, quién es y qué intenta hacer.

## ¿En qué se equivoca?

A veces interpreta mal una pantalla: 3 de los 20 agentes de LocalSend señalaron el teclado en inglés del simulador como parte de la app. Unos minutos por agente cubren los caminos principales, no cada rincón de una app grande. Cada hallazgo viene con capturas numeradas, así que revísalas antes de reportar nada.

## Límites

- Los runners de GitHub son gratis para repositorios públicos: unos 20 trabajos a la vez, 5 en macOS.
- En planes con un límite de uso de 5 horas, 20 agentes pueden agotarlo en ~15 min: ejecuta tandas de 6 a 10.
- Los runners alojados están pensados para el proyecto del propio repositorio. Para una app de código cerrado, ejecuta el workflow en tu repositorio privado o en tu propio Mac.

## Cómo funciona

<p align="center"><img src="../assets/how-it-works.svg" alt="Cómo funciona: un workflow compila la app, luego un emulador o simulador con un agente por persona, informes cifrados, resumen en tu máquina" width="100%"></p>

- **Las personas** definen el dispositivo: modelo, sistema, tamaño de letra, modo oscuro, idioma, ubicación.
- **Tres herramientas por agente**: ver la pantalla (con coordenadas para tocar), gestos, escribir.
- **Revisión de accesibilidad** en cada pantalla: controles sin nombre y zonas táctiles por debajo de 48 dp (Android) o 44 pt (iOS), que el agente confirma en la captura.
- **Resultados cifrados**: los logs de un repositorio público son públicos, así que todo se cifra con tu clave.
- **Analítica bloqueada** dentro de los teléfonos, para que las pruebas nunca toquen tus estadísticas reales.
- **Un resumen** en tu máquina: Claude agrupa los informes que describen el mismo error, así ves cuántas personas encontraron cada uno y qué personas encontraron cada tipo de problema.
- **Pruebas** en cada push, sin conexión y sin teléfono: revisión de accesibilidad, matriz de personas, resumen, resultados cifrados ([tests/](../tests/)).

## ¿Por qué no Maestro, Appium o agent-device?

Ejecutan las pruebas que tú escribes. Estos agentes buscan lo que nadie pensó en probar.

| | mobile-agent-testers | Maestro, Appium, Detox, e2e |
|---|---|---|
| Tú escribes | Nada: eliges personas de la lista | Flujos o código de prueba |
| Detecta | Flujos rotos, errores silenciosos, textos sin traducir, diseño con texto grande, modo oscuro, textos confusos | Lo que comprueba cada prueba |
| Mismo resultado en cada ejecución | No: cada ejecución explora, así que revisa las capturas | Sí |

[agent-device](https://github.com/callstackincubator/agent-device) da a un agente de programación el control de un simulador. Esto ejecuta una sesión completa: compila la app, da a cada persona su propio dispositivo y recoge informes cifrados. Usa agentes antes de una versión y flujos con script para las regresiones.

Comparativa completa, con Firebase Test Lab Robo, mobile-mcp, phonedriver y beta testers humanos: [docs/compare.md](compare.md) (en inglés).
