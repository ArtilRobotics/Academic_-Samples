#include <Servo.h>


String strT = "";
const char separatorT = ',';
const int dataLengthT = 2;
int datoT[dataLengthT];

Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int valpot;    // variable to read the value from the analog pin

int LDRpin =1;  // analog pin used to connect the potentiometer
int valLDR;    // variable to read the value from the analog pin

int RedLed_pin = 12;  // analog pin used to connect the potentiometer
int GreenLed_pin= 11;    // variable to read the value from the analog pin

int Boton1= 3;    // Boton Set 0
int Boton2= 4;    // Boton Set 0
int Boton3= 5;    // Boton Set 0
int Boton4= 6;    // Boton Set 0
int LDRMax=60;
int LDRMin=0;

bool Pot_Input=true;
int Slider_input=0;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(RedLed_pin,OUTPUT);
  pinMode(GreenLed_pin,OUTPUT);
  pinMode(Boton1,INPUT);
  pinMode(Boton2,INPUT);
  pinMode(Boton3,INPUT);
  pinMode(Boton4,INPUT);
  Serial.begin(9600);
}

void loop() {

  strT = "";
  if (Serial.available())
  {
    strT = Serial.readStringUntil('\n');
    Serial.println(strT);
    for (int i = 0; i < dataLengthT; i++)
    {
      int index = strT.indexOf(separatorT);
      datoT[i] = strT.substring(0, index).toInt();
      strT = strT.substring(index + 1);
    }
    for (int i = 0; i < dataLengthT; i++)
    {
      Serial.print("Dato "); 
      Serial.print(i);
      Serial.print("="); 
      Serial.print(datoT[i]);
    }
    Serial.println(" ");

    Pot_Input=datoT[0];
    Slider_input=datoT[1];
  }

  


/////////////
  if(Pot_Input){
    valpot = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
    valpot = map(valpot, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  }
  else{
    valpot=Slider_input;
  }

  myservo.write(valpot);                  // sets the servo position according to the scaled value
  
  valLDR = analogRead(LDRpin);            // reads the value of the potentiometer (value between 0 and 1023)
  valLDR = map(valLDR, 0, 1023, 100, 0); 
  
  if (digitalRead(Boton1) ==0){
      LDRMax=0;
  }

  if (digitalRead(Boton2) ==0){
      LDRMax=LDRMax+20;
  }

  if (digitalRead(Boton3) ==0){
      LDRMax=LDRMax+40;
  }

  if (digitalRead(Boton4) ==0){
      LDRMax=LDRMax+60;
  }

  if(LDRMax<0){
      LDRMax=0;
  }
  else if(LDRMax>100){
      LDRMax=100;
  }

  if(LDRMax>=40 ){
    LDRMin=LDRMax-40;
  }
  else{
    LDRMin=0;
  }


  if(valLDR>=LDRMax){
    digitalWrite(RedLed_pin, HIGH);
    }
    else
    {digitalWrite(RedLed_pin, LOW);
    }

  if(valLDR<=LDRMin){
    digitalWrite(GreenLed_pin, HIGH);
    }
    else
    {digitalWrite(GreenLed_pin, LOW);
    }

  Serial.print(valpot);
  Serial.print(",");
  Serial.print(valLDR);
  Serial.print(",");
  Serial.print(LDRMax);
  Serial.print(",");
  Serial.print(LDRMin);
  Serial.println("");
  delay(100);                           // waits for the servo to get there
}