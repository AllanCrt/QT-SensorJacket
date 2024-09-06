int sensorPin1 = A0;   // select the input pin for the first potentiometer
int sensorPin2 = A1;   // select the input pin for the second potentiometer
int sensorPin3 = A2;   // select the input pin for the third potentiometer
int sensorPin4 = A3;   // select the input pin for the fourth potentiometer
int sensorPin5 = A4;   // select the input pin for the fifth potentiometer
int sensorPin6 = A5;   // select the input pin for the sixth potentiometer
int sensorPin7 = A6;   // select the input pin for the seventh potentiometer
int sensorPin8 = A7;   // select the input pin for the eighth potentiometer
int ledPin = 13;       // select the pin for the LED
int sensorValue1 = 0;  // variable to store the value coming from the first sensor
int sensorValue2 = 0;  // variable to store the value coming from the second sensor
int sensorValue3 = 0;  // variable to store the value coming from the third sensor
int sensorValue4 = 0;  // variable to store the value coming from the fourth sensor
int sensorValue5 = 0;  // variable to store the value coming from the fifth sensor
int sensorValue6 = 0;  // variable to store the value coming from the sixth sensor
int sensorValue7 = 0;  // variable to store the value coming from the seventh sensor
int sensorValue8 = 0;  // variable to store the value coming from the eighth sensor

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int useCase = 1; // 1 - RA, 2 - RF, 3 - B, 4 - LA, 5 - all

  if (useCase == 1) {
    // Case 1: Read and print RA - P and RA - T
    sensorValue1 = analogRead(sensorPin1); // RA - P
    sensorValue5 = analogRead(sensorPin5); // RA - T
    Serial.print(sensorValue1); 
    Serial.print(",");
    Serial.println(sensorValue5);
  }

  if (useCase == 2) {
    // Case 2: Read and print RF - P and RF - T
    sensorValue2 = analogRead(sensorPin2); // RF - P
    sensorValue6 = analogRead(sensorPin6); // RF - T
    Serial.print(sensorValue2);
    Serial.print(",");
    Serial.println(sensorValue6);
  }

  if (useCase == 3) {
    // Case 3: Read and print B - P and B - T
    sensorValue3 = analogRead(sensorPin3); // B - P
    sensorValue7 = analogRead(sensorPin7); // B - T
    Serial.print(sensorValue3);
    Serial.print(",");
    Serial.println(sensorValue7);
  }

  if (useCase == 4) {
    // Case 4: Read and print LA - P and LA - T
    sensorValue4 = analogRead(sensorPin4); // LA - P
    sensorValue8 = analogRead(sensorPin8); // LA - T
    Serial.print(sensorValue4);
    Serial.print(",");
    Serial.println(sensorValue8);
  }

  if (useCase == 5) {
    // Case 5: Read and print all sensors
    sensorValue1 = analogRead(sensorPin1); // RA - P
    sensorValue2 = analogRead(sensorPin2); // RF - P
    sensorValue3 = analogRead(sensorPin3); // B - P
    sensorValue4 = analogRead(sensorPin4); // LA - P
    sensorValue5 = analogRead(sensorPin5); // RA - T
    sensorValue6 = analogRead(sensorPin6); // RF - T
    sensorValue7 = analogRead(sensorPin7); // B - T
    sensorValue8 = analogRead(sensorPin8); // LA - T

    Serial.print(sensorValue1);
    Serial.print(",");
    Serial.print(sensorValue2);
    Serial.print(",");
    Serial.print(sensorValue3);
    Serial.print(",");
    Serial.print(sensorValue4);
    Serial.print(",");
    Serial.print(sensorValue5);
    Serial.print(",");
    Serial.print(sensorValue6);
    Serial.print(",");
    Serial.print(sensorValue7);
    Serial.print(",");
    Serial.println(sensorValue8);
  }

  // stop the program for a short time
  delay(20);
}
