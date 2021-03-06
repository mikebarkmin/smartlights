#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library (you most likely already have this in your sketch)

#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <ArduinoJson.h>

const char* ssid     = "gateway-xx";
const char* password = "xxx";

ESP8266WebServer server(80);

const int PIN_R = D0;
const int PIN_G = D1;
const int PIN_B = D2;

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

  analogWrite(PIN_R, r);
  analogWrite(PIN_G, g);
  analogWrite(PIN_B, b);

  server.send(200, "application/json", "{\"success\": true}");
}

void setup(void){
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  pinMode(PIN_R, OUTPUT);
  analogWrite(PIN_R, r);

  pinMode(PIN_G, OUTPUT);
  analogWrite(PIN_G, g);

  pinMode(PIN_B, OUTPUT);
  analogWrite(PIN_B, b);

  server.on("/leds", HTTP_GET, getLeds);
  server.on("/leds", HTTP_POST, setLeds);

  server.begin();
}

void loop(void){
  server.handleClient();
}
