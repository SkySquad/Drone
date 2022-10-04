#ifndef motor_control_h
#define motor_control_h

<<<<<<< HEAD
#include <Servo.h>

class BrushlessMotor{
    private:
        Servo motorType;
        int spd;                        //range of 0 - 1000
        int pin;
    public:
        BrushlessMotor(int pin);
        void writeMotor(void);          //write private var speed to motor
        void setSpd(int spd);         //public method to set speed of motor
};

#endif
=======
class BrushlessMotor{
    private:
        Servo motorType;
        int speed;                      //range of 0 - 1000
        void writeMotor(void);          //write private var speed to motor
        int pin;
    public:
        BrushlessMotor(int pin);
        void setSpeed(int speed);       //public method to set speed of motor
}

extern BrushlessMotor motor_control;

#endif
>>>>>>> 3516017 (mod README and rebasing)
