#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *
rightMotor = LargeMotor(OUTPUT_C)
leftMotor  = LargeMotor(OUTPUT_B)
ts = TouchSensor(INPUT_4);	assert ts.connected
cs = ColorSensor(INPUT_3);	assert cs.connected
us  = UltrasonicSensor(INPUT_1);	assert us.connected
cs.mode = 'COL-COLOR'
def motor_move(leftSpeed,rightSpeed):
	leftMotor.run_forever(speed_sp=leftSpeed)
	rightMotor.run_forever(speed_sp=rightSpeed)
btn = Button()
status=0
while not btn.any():
    if ts.value():
        if status!=1:
            status=1
            motor_move(-1000,-1000)
    elif us.value()<500:
        if status!=2:
            status=2
            motor_move(1000,1000)
            if us.value()>400:
                motor_move(-500,500)
                sleep(1)
            motor_move(1000,1000)
    elif cs.value() == 1:
        if status!=3:
            status=3
            motor_move(-1000,-1000)
            sleep(0.6)
    else:
        if status!=4:
            motor_move(500,-500)
            status=4
rightMotor.stop()
leftMotor.stop()
