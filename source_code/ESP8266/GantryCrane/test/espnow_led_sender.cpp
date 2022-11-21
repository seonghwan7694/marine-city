// Testing ESP-NOW protocol with LED (Sender)

#include <ESP8266WiFi.h>
#include <espnow.h>


const unsigned long delay_time = 2000;
uint8_t receiver_address[] = {0x58, 0xbf, 0x25, 0xdb, 0x66, 0x55};  // MAC Address of receiver


typedef struct SendData {
    bool led;
} SendData;


// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t send_status) {
    Serial.print("Last Packet Send Status: ");
    if (send_status == 0){
        Serial.println("Delivery success");
    }
    else{
        Serial.println("Delivery fail");
    }
}

x
void setup() {
    Serial.begin(115200);

    WiFi.mode(WIFI_STA);

    if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
    }

    esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
    esp_now_register_send_cb(OnDataSent);
    esp_now_add_peer(receiver_address, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}


void loop() {
    static int last_time;

    String serial_data;
    SendData send_data;

    if (Serial.available() > 0) {
        serial_data = Serial.read();

        if ((millis() - last_time) > delay_time) {
            if (serial_data == "On") send_data.led = true;
            else if (serial_data == "Off") send_data.led = false;
            else return;

            esp_now_send(receiver_address, (uint8_t *) &send_data, sizeof(send_data));

            last_time = millis();
        }
    }
}