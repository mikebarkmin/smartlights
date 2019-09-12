import express from 'express';
import http from 'http';
import path from 'path';
import cors from 'cors';

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
const server = http.createServer(app);

app.use(cors());
app.use(express.json());

server.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

const lights = {};

app.get('/', (req, res) => {
  res.sendFile('index.html', { root: __dirname });
});

app.get('/lights', (req, res) => {
  res.send(lights);
});

app.get('/leds', (req, res) => {
  const hostname = req.hostname;
  if (hostname) {
    let light = { r: 0, g: 0, b: 0 };
    if (lights[hostname]) {
      light = lights[hostname];
    } else {
      lights[hostname] = light;
    }
    return res.send(light);
  }
  res.status(400).send('hostname not found');
});

app.post('/leds', (req, res) => {
  const hostname = req.hostname;
  if (hostname) {
    let light = req.body;
    lights[hostname] = { ...lights[hostname], ...light };
    return res.send(light);
  }
  res.status(400).send('hostname not found');
});
