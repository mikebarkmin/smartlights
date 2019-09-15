#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library (you most likely already have this in your sketch)

#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <WiFiManager.h>          //https://github.com/tzapu/WiFiManager WiFi Configuration Magic
#include <ArduinoJson.h>
#include <Adafruit_NeoPixel.h>

WiFiManager wifiManager;

ESP8266WebServer server(80);

const int NUMBER_OF_PIXEL = 6;
const int PIN = D1;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_OF_PIXEL, PIN, NEO_GRB + NEO_KHZ800);

double r = 0;
double g = 0;
double b = 0;

void getLeds() {
  // 200 kb calculated with https://arduinojson.org/v5/assistant/
  StaticJsonDocument<200> jsonBuffer;
  JsonObject leds = jsonBuffer.to<JsonObject>();

  leds["r"] = r;
  leds["g"] = g;
  leds["b"] = b;

  char message[200];

  serializeJson(leds, message);
  
  server.send(200, "application/json", message);
}

void setLeds() {
  StaticJsonDocument<200> jsonBuffer;
  deserializeJson(jsonBuffer, server.arg("plain"));
  
  JsonObject leds = jsonBuffer.as<JsonObject>();

  r = constrain(leds["r"].as<double>() * 1023 / 255, 0, 1023);
  g = constrain(leds["g"].as<double>() * 1023 / 255, 0, 1023);
  b = constrain(leds["b"].as<double>() * 1023 / 255, 0, 1023);

  for (int i=0; i < NUMBER_OF_PIXEL; i++) {
    strip.setPixelColor(i, r, g, b);
  };
  strip.show();

  server.send(200, "application/json", "{\"success\": true}");
}

void setup(void){
  Serial.begin(115200);
  
  wifiManager.autoConnect();
  
  strip.begin();
  strip.show();

  server.on("/leds", HTTP_GET, getLeds);
  server.on("/leds", HTTP_POST, setLeds);

  server.begin();
}

void loop(void){
  server.handleClient();
}
