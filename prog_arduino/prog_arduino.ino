#include "DHT.h"

#define DHTTYPE DHT11

#define DHTPIN 2
DHT dht(DHTPIN, DHTTYPE);


#if defined(ARDUINO_ARCH_AVR)
    #define serial  Serial

#elif defined(ARDUINO_ARCH_SAMD) ||  defined(ARDUINO_ARCH_SAM)
    #define serial  SerialUSB
#else
    #define serial  Serial
#endif

void setup() {
    serial.begin(115200);
    Wire.begin();
    dht.begin();
}

void loop() {
    float temp_hum_val[2] = {0};

    if (!dht.readTempAndHumidity(temp_hum_val)) {
        serial.print("Humidity: ");
        serial.print(temp_hum_val[0]);
        serial.print(" %\n");
        serial.print("Temperature: ");
        serial.print(temp_hum_val[1]);
        serial.println(" *C");
    } else {
        serial.println("Failed to get temprature and humidity value.");
    }

    delay(300000);
}
