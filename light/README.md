# Light

Die Glühbirnen stellt ein HTTP-Interface zur Verfügung über das ihr
Zustand geändert werden kann.

## REST API

| Methode | Endpunkte | Parameter                              | Antwort                                  | Beschreibung        |
|--------|----------|-----------------------------------------|-------------------------------------------|--------------------|
| GET    | /leds    |                                         | `[{"r": <int>, "g": <int>, "b": <int> }]` | Gibt den Zustand der LEDs     |
| POST   | /leds    | `{"r": <int>, "g": <int>, "b": <int> }` |                                           | Zustand der LEDs setzen |

## Implementierungen

* [ESP-8266](esp8266)
  * [Arduino](esp8266/arduino)
* [Raspberry Pi Zero](raspberry_pi_zero)
  * [Java](raspberry_pi_zero/java)
  * [Python](raspberry_pi_zero/python)
* [Simulator](simulator/java)

## Testen

Natürlich kann die Implementierung der smarten Glühbire im gesamten System
getestet werden. Es ist aber auch möglich die smarte Glühbirne unabhängig vom
restlichen System zu testen, indem die einzelnen Endpunkte aufgerufen werden.
Zum Beispiel mit:

* Android: [RestClient](https://play.google.com/store/apps/details?id=com.app.restclient&hl=en_US)
* Desktop: [Insomnia](https://insomnia.rest) importiere [insomnia](insomnia.json) oder lege die Anfragen neu an
* Terminal: [Curl](https://curl.haxx.se/) `curl http://localhost:8080` oder `curl --header "Content-Type: application/json" --request POST --data '{"r": 100,"g": 0, "b": 20}' http://localhost:8080/leds`
