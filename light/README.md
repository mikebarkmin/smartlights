# REST Api

| Method | Endpoint | Parameters                              | Response                                  | Description        |
|--------|----------|-----------------------------------------|-------------------------------------------|--------------------|
| GET    | /leds    |                                         | `[{"r": <int>, "g": <int>, "b": <int> }]` | Status of leds     |
| POST   | /leds    | `{"r": <int>, "g": <int>, "b": <int> }` |                                           | Set status of leds |