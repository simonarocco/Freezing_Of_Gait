#include <Wire.h>

int mpu = 0x68; // I2C address of the MPU-6050
float AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
float minimumRange[] = {-32684.8, -27684.84}; //holds lower and upper bound of minimum range //previous -34768, -32000
float absPeakDiffRange[] = {21498.3, 28498.3}; //previous 30000, 32500
float shuffleMinArray[100];
float shufflePeakArray[100];
int indexShuffle = 0;
int shuffleMinCount = 0;
int shufflePeakCount = 0;
float smoothedSignal[80];
float minimum = 0;
float maximum = -30000;
int pinLED = 13;
float window[6];
float meanWindow = 0;

void setup() {

  Wire.begin();
  Wire.beginTransmission(mpu);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200);
  pinMode(pinLED, OUTPUT);

}

void loop() {
  int count = 0;
  for(int j = 0; j < 85; j++) {
      Wire.beginTransmission(mpu);
      Wire.write(0x3B);
      Wire.endTransmission(false);
      Wire.requestFrom(mpu, 14, true);
      Serial.print("Acc x: ");
      AcX = Wire.read()<<8|Wire.read();
      Serial.println(AcX);
      //Serial.print("Acc y: ");
      AcY = Wire.read()<<8|Wire.read();
      //Serial.println(AcY);
      //Serial.print("Acc z: ");
      AcZ = Wire.read()<<8|Wire.read();
      //Serial.println(AcZ);
      for(int i = 0; i < 5; i++) {
        window[i] = window[i+1];
      }
      window[5] = AcX;
      for(int u = 0; u < 6; u++) {
        //Serial.println(window[u]);
      }
      //delay(1000);
      if(window[0] != NULL) {
      smoothedSignal[j] = meanFull(window);
      //Serial.print("smoothed signal: ");
      //Serial.println(smoothedSignal[j]);
      }
  }

  //delay(10000);
  //counter for min and maxes
  int j = 0;
  minimum = 0;
  maximum = -30000;
  float absPeakDiff = 0;
  while(j<80){
    if(smoothedSignal[j]<minimum) {
      minimum = smoothedSignal[j];
    }
    if(smoothedSignal[j]>maximum) {
      maximum = smoothedSignal[j];
    }
    j++;
  }
  absPeakDiff = maximum - minimum;
  Serial.print("Minimum: ");
  Serial.println(minimum);
  Serial.print("Maximum");
  Serial.println(maximum);
  Serial.print("Peak diff: ");
  Serial.println(absPeakDiff);
  
if(minimum>minimumRange[1] || minimum<minimumRange[0]){ //shuffle detected
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
   else if(absPeakDiff>absPeakDiffRange[0] && absPeakDiff<absPeakDiffRange[1]){
      shufflePeakArray[indexShuffle] = 0;
      shufflePeakCount = 0;
      }
    Serial.print("Shuffle Minimums: ");
    Serial.println(shuffleMinCount);
    Serial.print("Shuffle Peak Diff: ");
    Serial.println(shufflePeakCount);
   if(shuffleMinCount>=2 && shufflePeakCount >=3){
    Serial.print("peak diff avg: ");
    Serial.println(mean(shufflePeakArray, indexShuffle));
    if (mean(shufflePeakArray, indexShuffle)<4000){
      Serial.println("STOP DETECTED");
      digitalWrite(pinLED, HIGH);
      delay(5000);
      digitalWrite(pinLED, LOW);
      delay(700);
      digitalWrite(pinLED, HIGH);
      delay(700);
      digitalWrite(pinLED, LOW);
      delay(700);
      digitalWrite(pinLED, HIGH);
      delay(700);
      digitalWrite(pinLED, LOW);
      delay(700);
      digitalWrite(pinLED, HIGH);
      delay(700);
      digitalWrite(pinLED, LOW);
      delay(700);
      digitalWrite(pinLED, HIGH);
      delay(700);
      digitalWrite(pinLED, LOW);
      delay(700);
      digitalWrite(pinLED, HIGH);
      delay(700);
      digitalWrite(pinLED, LOW);
      delay(700);
    }
    else{
      Serial.println("SHUFFLE DETECTED");
      digitalWrite(pinLED, HIGH);
      delay(1000);
    }
    shuffleMinCount = 0;
    shufflePeakCount = 0;
   }
   if(indexShuffle>=100) indexShuffle = 0;
   else indexShuffle++;
}

float mean(float signalArray[], int index){
  return (signalArray[index]+signalArray[index-1])/2.0;
}

float meanFull(float arrays[]){
  float sum = 0;
  for(int i = 0; i < 6; i++){
    sum += arrays[i];
  }
  return sum/6; 
}
