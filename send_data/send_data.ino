const int currentSensorPin = 34; // GPIO34 for ADC
float sensitivity = 0.185;       // Sensitivity for ACS712 (e.g., 0.185V/A for 5A model)
float vOffset = 2.5;             // ACS712 zero current voltage at 5V (default is ~2.5V)
float adcResolution = 4096.0;    // ESP32 ADC resolution (12-bit)
float vRef = 5.0;                // Reference voltage when powered by VIN (5V)

float zeroCurrentVoltage = 0.0;  // Store the voltage when there is no load

void setup() {
  Serial.begin(9600);
  analogReadResolution(12); // Set ADC resolution to 12 bits

  // Read zero current voltage at startup (without any load)
  zeroCurrentVoltage = (analogRead(currentSensorPin) / adcResolution) * vRef;
}

void loop() {
  int rawValue = analogRead(currentSensorPin); // Read ADC value
  float sensorVoltage = (rawValue / adcResolution) * vRef; // Convert to voltage

  // Calculate current with respect to the zero current voltage
  float current = (sensorVoltage - zeroCurrentVoltage) / sensitivity;

  Serial.print("Raw ADC Value: ");
  Serial.print(rawValue);
  Serial.print("\t Sensor Voltage: ");
  Serial.print(sensorVoltage, 3);
  Serial.print(" V\t Measured Current: ");
  Serial.print(current, 3);
  Serial.println(" A");

  delay(1000); // Read every second
}
