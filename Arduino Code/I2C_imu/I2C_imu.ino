#include <Wire.h>
#include <math.h>
#define M_PI 3.14159265358979323846
int mpu = 0x68; // I2C address of the MPU-6050
int led = 13;
float AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
float sampleArrayAcx[80]; //sample array holding 80 Acx 
int count = 0; //use to fill up sample array 
float minimumRange[] = {21498.266666666666, 28498.266666666666}; //holds lower and upper bound of minimum range
double absPeakDiffRange[] = {-32684.8, -27684.8};
float shuffleMinArray[50];
float shufflePeakArray[50];
int indexShuffle = 0;
int shuffleMinCount = 0;
int shufflePeakCount = 0;

//calibration with 1000 samples
//bool calibrated = false;
void setup() {
  Wire.begin();
  Wire.beginTransmission(mpu);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}

void loop() {
//  if(calibrated == false){
//    calibrate();
//    Serial.println("Done calibrated");
//    calibrated = true;
//  }
  
  //createSampleLength80();
  //counter for min and maxes
  int i =0;
  int j = 0;
  int k = 80;
  float minimum = 0.0;
  float maximum = -40000.0;
  float absPeakDiff = 0.0;
  while(j<k){
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
  if(absPeakDiff<absPeakDiffRange[0] || absPeakDiff>absPeakDiffRange[1]){ //shuffle detected
      shufflePeakArray[indexShuffle]=absPeakDiff;
      shufflePeakCount ++;
  }
  else if(absPeakDiff>absPeakDiffRange[0] && absPeakDiff<absPeakDiffRange[1]){ //no shuffle detected
      shufflePeakArray[indexShuffle] = 0;
      shufflePeakCount = 0;
  }
  
  if(shuffleMinCount>=4 && shufflePeakCount >=4){
    if (mean(sampleArrayAcx)<300){
      Serial.println("STOP DETECTED");
    }
    else{
      Serial.println("SHUFFLE DETECTED");
    }
    shuffleMinCount = 0;
    shufflePeakCount = 0;
  }

  if(indexShuffle>=50) indexShuffle = 0;
  else indexShuffle++;
}

float mean(float signalArray[]){
  float mean = (sampleArrayAcx[79]+sampleArrayAcx[78]+sampleArrayAcx[77])/3.0;
  return mean;
}

float createSampleLength80(){
  int i = 0;
  while(i<80){
    Wire.beginTransmission(mpu);
    Wire.write(0x3B);
    Wire.endTransmission(false);
    Wire.requestFrom(mpu, 14, true);
    //Serial.print("Acc x: ");
    Wire.beginTransmission(mpu);
    Wire.write(0x3B);
    Wire.endTransmission(false);
    Wire.requestFrom(mpu, 14, true);
    AcX = Wire.read()<<8|Wire.read();
    sampleArrayAcx[i] = AcX;
    //delay(10);
    i++;
  }
}

float getAcX(){
  Wire.beginTransmission(mpu);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(mpu, 14, true);
  AcX = Wire.read()<<8|Wire.read();
  AcY = Wire.read()<<8|Wire.read();
  AcZ = Wire.read()<<8|Wire.read();
  Tmp = Wire.read()<<8|Wire.read();
  GyX = Wire.read()<<8|Wire.read();
  GyY = Wire.read()<<8|Wire.read();
  GyZ = Wire.read()<<8|Wire.read();
  return AcX;
}

//void calibrate(){
//  Serial.println("Calibrating");
//  float callAcx[80][10];
//  int i = 0;
//  int j = 0;
//  float minimums[10];
//  float maximums[10];
//  float minimumC = 0.0;
//  float maximumC = -30000.0;
//  while(i<10){
//    for(int a=0; a<80; a++){
//      //callAcx[a][i] = getAcX();
//      //Serial.println(AcX);
//      Serial.println(a);
//      delay(10);
//    }
//    Serial.println("Done for loop");
//    while(j<80){
//      if(callAcx[j][i] < minimumC) minimumC = callAcx[j][i];
//      if(callAcx[j][i] > maximumC) maximumC = callAcx[j][i];
//      j++;
//      Serial.println("entered while loop");
//    }
//    minimums[i] = minimumC;
//    maximums[i] = maximumC;
//    Serial.print("The minimum found is");
//    Serial.print(minimumC);
//    Serial.print("The maximum found is");
//    Serial.print(maximumC);
//    i++;
//  }
//  //create range for each feature
//  minimumRange[0] = meanFull(minimums) - 2000;
//  minimumRange[1] = meanFull(minimums) + 3000;
//
//  float peakDiff[10];
//    for(int i = 0; i <10; i++){
//      peakDiff[i] = maximums[i]-minimums[i];
//    }
//  absPeakDiffRange[0] = meanFull(peakDiff) - 5000;
//  absPeakDiffRange[1] = meanFull(peakDiff) + 2000;
//      
//  Serial.print("Minimum Range lower bound");
//  Serial.println(minimumRange[0]);
//  Serial.print("Minimum range upper bound");
//  Serial.println(minimumRange[1]);
//  Serial.print("Peak Diff Range lower bound");
//  Serial.println(absPeakDiffRange[0]);
//  Serial.print("Peaks diff range upper bound");
//  Serial.println(absPeakDiffRange[1]);
//}

float meanFull(float arrays[10]){
  float sum = 0;
  float mean = 0;
  for(int i = 0; i < sizeof(arrays); i++){
    sum += arrays[i];
  }
  return mean = sum/sizeof(arrays); 
}
