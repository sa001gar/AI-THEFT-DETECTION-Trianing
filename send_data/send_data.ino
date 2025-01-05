#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Virus Detected";
const char* password = "Sagar@react";
const char* serverUrl = "http://192.168.1.36:3000/data";

const int sensorPin = 35;  // GPIO 36 (ADC1_CH0)

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  float current = readCurrent();
  float power = calculatePower(current);
  
  String data = String(current, 3) + "," + String(power, 3);
  sendData(data);
  
  delay(5000); // Send data every 5 seconds
}

float readCurrent() {
  int sensorValue = analogRead(sensorPin);
  float voltage = sensorValue * (3.3 / 4095.0);
  float current = (voltage - 1.65) / 0.185; // For ACS712 10A version
  return current;
}

float calculatePower(float current) {
  float voltage = 12.0; // Assuming a stable 12V supply
  return voltage * current;
}

void sendData(String data) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    int httpResponseCode = http.POST("data=" + data);
    
    if (httpResponseCode > 0) {
      Serial.println("Data sent successfully");
    } else {
      Serial.println("Error sending data");
    }
    
    http.end();
  }
}

