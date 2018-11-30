#include <Wire.h>
#include <math.h>
#define M_PI 3.14159265358979323846
int mpu = 0x68; // I2C address of the MPU-6050
int led = 13;
float AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
float sampleArrayAcx[80]; //sample array holding 80 Acx 
count = 0; //use to fill up sample array 
float minimumRange[] = {21498.266666666666, 28498.266666666666}; //holds lower and upper bound of minimum range
float absPeakDiffRange[] = {-32684.8, -27684.8};
float shuffleMinArray[600];
float shufflePeakArray[600];
int indexShuffle = 0;
int shuffleMinCount = 0;
int shufflePeakCount = 0;
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
  while(count<80){
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
    delay(10);
    sampleArratAcx[count] = Acx;
    count++;
  }
  //counter for min and maxes
  int i =0;
  int j = 0;
  int k = 80;
  float minimum = 0.0;
  float maximum = -40000.0;
  float absPeakDiff = 0.0;
  while(j<=k){
      if(sampleArrayAcx[j]<minimum) minimum = sampleArrayAcx[j];
      if(sampleArrayAcx[j]>maximum) maximum = sampleArrayAcx[j];
      absPeakDiff = maximum - minimum;
      j++;
      }
  if(minimum>minimumRange[1]){ //shuffle detected
      shuffleMinArray[indexShuffle] = minimum;
      shuffleMinCount ++;
      }
  else if (minimum>minimumRange[0] && minimum<minimumRange[1]){ //no shuffle detected
       shuffleMinArray[indexShuffle] = 0;
       shuffleMinCount = 0;
       }
  if(absPeakDiff<absPeakDiffRange[0] || absPeakDiff>absPeakDiffRange[1]){
      shufflePeakArray[indexShuffle]=absPeakDiff;
      shufflePeakCount ++;
      }
   else if(absPeakDiff>absPeakDiff[0] && absPeakDiff<absPeakDiff[1]){
      shufflePeakArray[indexShuffle] = 0;
      shufflePeakCount = 0;
      }
   if(shuffleMinCount>=4 && shufflePeakCount >=4){
    if 
      }
   if(indexShuffle>=600) indexShuffle = 0;
   else indexShuffle++;
   
  
}

