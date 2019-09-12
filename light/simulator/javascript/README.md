# Simulator

Der Javascript Simulator ist darauf ausgelegt mehrere Glühbirnen gleichzeitig
zu simulieren. Dafür wird mit Subdomains gearbeitet. Es wird automatisch wenn
eine Subdomain angesteuert wird eine neue Glühbirne angelegt. Damit dies
gelingen kann muss ein Proxy den Traffic von `*.mydomain.com` zur Anwendung
weiterleiten. Siehe `docker-compose.yml` als Beispiel.

## Development

```
docker-compose up
```

## Deployment

Without docker
```
yarn build
cp build/server.js to_server
cp package.json to_server
yarn install
node server.js
```

With docker
```
docker run -d --name smartlights-simulator -p 8080:8080 mikebarkmin/smartlights-simulator
```

