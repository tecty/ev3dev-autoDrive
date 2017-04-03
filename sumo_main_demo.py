#！、usr/bin/env python3
# to use python3 in ev3

from time import sleep
import sys, os

from ev3dev.ev3 import *
from motor import *

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor = LargeMotor(OUTPUT_C)
middleMotor = LargeMotor(OUTPUT_A)

#Connect sensors
us = UltrasonicSensor();	assert us.connected
cs = ColorSensor();			assert cs.connected
gs = GyroSensor();			assert gs.connected

us.mode = 'US-DIST-CM' #change the mode of the ultra sonic sensor into the distance mode
cs.mode = 'COL-COLOR' #change the mode of the color sensor into the color mode
gs.mode = 'GYRO-RATE' #change the mode of the gyro sensor into the rate mode

#We will need to check EV3 button state.
btn = Button()

begin = False

#hold for 3 seconds
def hold_3sec_start():
	global begin

	if not begin:
		sleep(3)
		motor_turnsAngle(angle,inputSpeed) #turn to the enemy after waiting
		begin = True

hold_3sec_start()
sonar_distance()
#Run the robot until a button is pressed.
while not btn.any():
	if not sonar_isEnemy()
		gyro_reset()
		motor_turns(dir,inputSpeed) #rotate to find the enemy
		if Gyro_isEnemy():
			motor_break()
			sleep(0.01)
			motor_straightMove(inputSpeed)

	else:
		motor_break()
		sleep(0.01)
		motor_straightMove(inputSpeed) #the enemy is in front of the robot

	if color_isEdge():
		motor_shrink_back(inputSpeed)
		motor_break()
		sleep(0.01)

#stop the motors before exiting.
motor_break()