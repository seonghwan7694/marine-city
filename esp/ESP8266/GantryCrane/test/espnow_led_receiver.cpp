// Testing ESP-NOW protocol with LED (Receiver)

#include <ESP8266WiFi.h>
#include <espnow.h>


typedef struct RecvData {
    bool led;
} RecvData;


void OnDataRecv(uint8_t * mac, uint8_t *incoming_data, uint8_t len) {
    RecvData recv_data;

    memcpy(&recv_data, incoming_data, sizeof(recv_data));
    if (Serial.available() > 0) {
        Serial.println(recv_data.led);
    }

    if (recv_data.led == true) {
        digitalWrite(LED_BUILTIN, HIGH);
    }

    if (recv_data.led == false) {
        digitalWrite(LED_BUILTIN, LOW);
    }
}
 
void setup() {
    Serial.begin(115200);

    WiFi.mode(WIFI_STA);

    if (esp_now_init() != 0) {
        Serial.println("Can't initalize ESP-NOW");
        return;
    }

    pinMode(LED_BUILTIN, HIGH);

    esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);
    esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
}
