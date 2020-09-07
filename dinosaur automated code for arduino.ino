
#define soundPin 8

int values;
;
 void setup()
 {

  pinMode(soundPin,INPUT); // declaration of soundsensor as a input
  Serial.begin(9600); //begin the serial monitor

 }

void loop ()
{


 values = digitalRead(soundPin); //read the value from the soundsensor and store in variable 
 Serial.println(values);//print the stored variable
 delay(100);//delay 100 millisecond
 
}
