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
