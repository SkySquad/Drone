<<<<<<< HEAD
=======
#include <Servo.h>

>>>>>>> 3516017 (mod README and rebasing)
#include "Arduino.h"
#include "motor_control.h"


<<<<<<< HEAD
BrushlessMotor::BrushlessMotor(int x) : pin(x) {
    motorType.attach(pin);
    motorType.writeMicroseconds(1000);
}

void BrushlessMotor::setSpd(int _spd){
    spd = _spd;
}

void BrushlessMotor::writeMotor(void){
    motorType.writeMicroseconds(map(spd, 0, 1000, 1000, 2000));             //write speed to servo (motorType of type Servo)
}
=======
BrushlessMotor::BrushlessMotor(int pin){
    self.pin = pin;
    self.motorType.attach(self.pin);
    self.motorType.writeMicroseconds(1000);
}

void BrushlessMotor::setSpeed(int speed){
    self.speed = speed;
    self.writeMotor();
}

void BrushlessMotor::writeMotor(void){
    int temp = map(speed, 0, 1000, 1000, 2000);
    motorType.writeMicroseconds(temp);
}


BrushlessMotor motor_control = BrushlessMotor();
>>>>>>> 3516017 (mod README and rebasing)
