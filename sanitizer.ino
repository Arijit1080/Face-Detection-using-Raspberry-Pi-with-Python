#include <Ultrasonic.h>

Ultrasonic ultrasonic(4, 5);

int pot1 = 2;
int pot2 = 3;
int piezoPin = 8;
int distance;
int t_distance;
int pump_delay;

void setup() {
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  digitalWrite(6, HIGH);
  delay(2000);
}

void loop() {
  
  pump_delay = analogRead(pot1);
  if (pump_delay == 0)
    pump_delay = 300;

  t_distance = analogRead(pot2);
  if (t_distance == 0)
    t_distance = 8;
  else
    t_distance = t_distance / 100;

  distance = ultrasonic.read();
  if(distance <= t_distance)
  {
    digitalWrite(6, LOW);
    digitalWrite(7, HIGH);
    tone( 8, 2000, 500);
    delay(pump_delay*2);
    digitalWrite(6, HIGH);
    digitalWrite(7, LOW);
    delay(2000); 
  }

}
