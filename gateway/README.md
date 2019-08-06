# REST Api

| Method | Endpoint        | Parameters                             | Response               | Description                    |
|--------|-----------------|----------------------------------------|------------------------|--------------------------------|
| GET    | /devices        |                                        | `[{"mac": <string> }]` | Get all devices on the network |
| POST   | /lights         | `{"mac": <string>, "name": <string> }` |                        | Add a new light                |
| PUT    | /lights/\<mac\> | `{"name": <string>}`                   |                        | Update a light                 |
| DELETE | /lights/\<mac\> |                                        |                        | Delete a light                 |

# Database

All information is stored in an [SQLite](https://sqlite.org) database.

## Entities

| light         |
|---------------|
| name : string |
| mac: string   |


