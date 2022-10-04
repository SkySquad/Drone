#include "Arduino.h"
#include "return_home.h"

//IR_sensor
#define IR_sensor_pin 4
bool isObstacle = HIGH;         //HIGH means no obstacle

//ultrasonic_sensor
#define echoPin 2
#define trigPin 3
long duration;                  //duration of sound
int distance;                   //distance measurement

rclass::rclass(){
}

bool rclass::returnHome();
//main function for returning home

void rclass::sensor_setup(){
    pinMode(IR_sensor_pin, INPUT);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

rclass return_home = rclass();