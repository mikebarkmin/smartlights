# ESP32 in Arduino IDE

To use the ESP32 board in the Arduino IDE we need to add a additional board manager url. See [https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md](https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md).

# Auto Connect to Wifi

To change the Wifi-connection easily and without flashing the microcontroller, we can use the library [WifiManager](https://github.com/tzapu/WiFiManager). For WifiManager to work with ESP32 we need to use the latest development branch of the project.

```
cd $ARDUINO_FOLDER/libraries
git clone https://github.com/tzapu/WiFiManager.git
git checkout development
```
