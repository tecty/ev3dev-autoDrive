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
motor_move(1000,-1000)
sleep(0.5)
rightMotor.stop()
leftMotor.stop()
