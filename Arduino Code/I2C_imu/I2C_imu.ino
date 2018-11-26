#include <Wire.h>
#include <math.h>
#define M_PI 3.14159265358979323846
int mpu = 0x68; // I2C address of the MPU-6050
int led = 13;
float AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.beginTransmission(mpu);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0);
  Wire.endTransmission(true);
  pinMode(led, OUTPUT);

}

void loop() {
  Wire.beginTransmission(mpu);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(mpu, 14, true);
   Serial.print("Acc x: ");
  AcX = Wire.read()<<8|Wire.read();
  Serial.println(AcX);
  Serial.print("Acc y: ");
  AcY = Wire.read()<<8|Wire.read();
  Serial.println(AcY);
  Serial.print("Acc z: ");
  AcZ = Wire.read()<<8|Wire.read();
  Serial.println(AcZ);
//  Serial.print("Angle: ");
//  float angle = acos(AcY/16384);
//  Serial.println(angle);
//  if ( angle >= M_PI/4){
//    digitalWrite(led, HIGH);
//  }
//  else digitalWrite(led, LOW);
//  Serial.print("Angle Y/Z: ");
//  double angle_y = atan2(AcZ,AcY);
  //Serial.println(angle*(180/M_PI));
//  Tmp = Wire.read()<<8|Wire.read();
//  Serial.print("The temperature is: ");
//  Serial.println(Tmp);
//  GyX = Wire.read()<<8|Wire.read();
//  Serial.print("Gyroscope in the X is: ");
//  Serial.println(GyX);
//  GyY = Wire.read()<<8|Wire.read();
//  GyZ = Wire.read()<<8|Wire.read();
  delay(10);
}
