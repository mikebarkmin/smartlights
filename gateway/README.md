# Basisstation

Die Basisstation besteht aus zwei Komponenten. Einem Webserver, welcher auf
verschiedene Anfragen reagiert und gegebenfalls Änderungen in der zweiten
Komponente der Datenbank vornimmt.

## Funktionen 

* Die Basisstation verwaltet die einzelnen Glühbirnen im selben Netzwerk
* Sie stellt ein Netzwerk zur Verfügung mit dem sich die Glühbirnen verbinden
* Neue Glühbirnen werden von der Basisstation nicht automatisch registriert
* Der Zustand der Glühbirnen wird über die Basisstation gesetzt

## Webserver

### REST API

| Methode | Endpunkte        | Parameter                             | Antwort               | Beschreibung                    |
|--------|-----------------|----------------------------------------|------------------------|--------------------------------|
| GET    | /devices        |                                        | `[ip_address]` | Gib alle IP-Adressen im Netzwerk |
| GET    | /lights        |                                        | `[light]` | Gib alle registrierten Glühbirnen |
| POST   | /lights         | `{"name": <string>, "ip_address": <string>, "port": <integer> }` |                        | Eine Glühbirne hinzufügen / registrieren               |
| PUT    | /lights/\<id\> | `{"name": <string>, "r": <integer>, "g": <integer>, "b": <integer>}`                   |                        | Eine Glühbirne updatend                 |
| DELETE | /lights/\<id\> |                                        |                        | Eine Glühbiren löschen                 |

## Datenbank

Alle Informationen werden in einer [SQLite](https://sqlite.org) Datenbank gespeichert.

### Entitäten

| light         |
|---------------|
| id: integer |
| name : string |
| ip_address: string   |
| port: integer |
| r: integer |
| g: integer |
| b: integer |

## Implementierungen

* [Desktop](desktop)
  * [Java](desktop/java)
  * [Node-RED](desktop/nodered)
  * [Python](desktop/python)

## Testen

Natürlich kann die Implementierung der Basisstation im gesamten System
getestet werden. Es ist aber auch möglich die Basisstation unabhängig vom
restlichen System zu testen, indem die einzelnen Endpunkte aufgerufen werden.
Zum Beispiel mit:

* Android: [RestClient](https://play.google.com/store/apps/details?id=com.app.restclient&hl=en_US)
* Desktop: [Insomnia](https://insomnia.rest) importiere [insomnia](insomnia.json) oder lege die Anfragen neu an
* Terminal: [Curl](https://curl.haxx.se/) `curl http://localhost:8000` oder `curl --header "Content-Type: application/json" --request POST --data '{"ip_address": "192.169.2.72", "port": "80", "name": "Schlafzimmer", r": 100,"g": 0, "b": 20}' http://localhost:8000/lights`
