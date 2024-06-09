//Speed Manual - ena110
//Front - Front0
//Back  - Back00
//Right - Right0
//Left  - Left00
//Stop  - Stop00

const int rainSensorPin = A0;


#include <SoftwareSerial.h>
SoftwareSerial mySerial(10,9); // RX, TX

#include <Servo.h>
Servo myservo;
int pos = 0;

int motor1_ena  = 3;
int motor2_enb  = 5;

#define IN1 2
#define IN2 4
#define IN3 6
#define IN4 7

char Motor_inputs[8];
String Motor_input;
String Speed_Value;
char Speed_Val[4];


const int trigPin = 12;
const int echoPin = 8;
long duration;
int distance;


void setup() {

  pinMode(rainSensorPin, INPUT);
  pinMode(IN1, OUTPUT);   //IN1
  pinMode(IN2, OUTPUT);   //IN2
  pinMode(IN3, OUTPUT);   //IN3
  pinMode(IN4, OUTPUT);   //IN4

  pinMode(motor1_ena, OUTPUT);
  pinMode(motor2_enb, OUTPUT);
  byte speed = 0;

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  mySerial.begin(9600);

}

void loop() { // run over and over

  ultra();


  if (mySerial.available()) {
    Motor_input = mySerial.readString(); //Stop00 , Front0, Back00, Left00, Right0, ena255, ena075
    Motor_input = Motor_input.substring(0, 6);
    Speed_Value = Motor_input.substring(3, 6);
  }

  for (int i = 0; i < 6; i++)
  {
    Motor_inputs[i] = Motor_input[i];
  }

  for (int i = 0; i < 3; i++)
  {
    Speed_Val[i] = Motor_input[i];
  }

  if (!strcmp(Speed_Val, "ena"))
  {
    analogWrite(motor1_ena, Speed_Value.toInt());
    analogWrite(motor2_enb, Speed_Value.toInt());
    Serial.print("Speed_Value");
    Serial.println(Speed_Value);
  }



  if (!strcmp(Motor_inputs, "Stop00"))
  {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, HIGH);
    Serial.println("stop");
    Serial.println("\n");

    Motor_input = "Hault";
    for (int i = 0; i < 6; i++)
    {
      Motor_inputs[i] = Motor_input[i];
    }
    Serial.println(Motor_inputs);
  }

  else if (!strcmp(Motor_inputs, "Front0"))
  {
    Serial.println("Front");
    Serial.println("\n");
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    rain();
  }
  else if (!strcmp(Motor_inputs, "Back00"))
  {
    Serial.println("Back");
    Serial.println("\n");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
  }
  else if (!strcmp(Motor_inputs, "Right0"))
  {
    Serial.println("Right");
    Serial.println("\n");
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
  }
  else if (!strcmp(Motor_inputs, "Left00"))
  {
    Serial.println("Left");
    Serial.println("\n");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
  }

  delay(100);
}

void servmtr() {
  myservo.attach(13);

  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }

  //myservo.detach();
}


void ultra() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  Serial.println(distance);

  if (distance >= 2 && distance <= 20) {
    
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, HIGH);
    Serial.println("stop");
    Serial.println("\n");

    Motor_input = "Hault";
    for (int i = 0; i < 6; i++)
    {
      Motor_inputs[i] = Motor_input[i];
    }
    Serial.println(Motor_inputs);
  }
}

void rain()
{
  int rain_val = analogRead(rainSensorPin);


  if (rain_val >= 400 && rain_val <= 800 ) {
    //Serial.println("Status: rain");
    servmtr();
  }


}
