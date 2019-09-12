# REST Api

| Method | Endpoint       | Parameters                                                   | Response       | Description                                    |
| ------ | -------------- | ------------------------------------------------------------ | -------------- | ---------------------------------------------- |
| GET    | /devices       |                                                              | `[ip_address]` | Get all ip addresses of devices on the network |
| GET    | /lights        |                                                              | `[ light ]`    | Get all lights                                 |
| POST   | /lights        | `{"ip_address": <string>, "port": <int>, "name": <string> }` |                | Add a new light                                |
| PUT    | /lights/\<id\> | `{"name": <string>, "r": <int>, "g": <int>, "b": <int>}`     |                | Update a light                                 |
| DELETE | /lights/\<id\> |                                                              |                | Delete a light                                 |

# Database

All information is stored in an [SQLite](https://sqlite.org) database.

## Entities

| light               |
|---------------------|
| name : string       |
| ip_address: string  |
| port: int           |
| r: int              |
| g: int              |
| b: int              |
