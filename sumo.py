#!/usr/bin/env python3
#to use python3 in ev3

from time import sleep
import sys, os

from ev3dev.ev3 import *

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)

# Connect touch sensors.
ts1 = TouchSensor(INPUT_1);	assert ts1.connected
ts4 = TouchSensor(INPUT_4);	assert ts4.connected
us  = UltrasonicSensor();	assert us.connected
gs  = GyroSensor();		assert gs.connected

gs.mode = 'GYRO-RATE'	# Changing the mode resets the gyro
gs.mode = 'GYRO-ANG'	# Set gyro mode to return compass angle

# We will need to check EV3 buttons state.
btn = Button()

#Run the robot until a button is pressed.
begin = 0

start()
while not btn.any():

	if begin = 0
		#hold for 3 seconds.
		sleep(3)
		
		#turn the robot to the left
		motor_turns(1,1000)
		
		begin = 1
		
	
	#If the robot is being pushed, it will fight back.	
	if(ts1.value() or ts4.value()):
		motor_reverse()
		
	#Ultrasonic sensor will find the enemy 
	#Measure the distance to the closest object in front of the robot.
	distance = us.value();

	if distance < 400:
		#The enemy is in front of the robot.
		motor_directMove(1000)
		"""
		Maybe need a speed up if the robot is close to the enemy.
		"""
	else:
		#The enemy is neither in front of the robot nor at the back.
		motor_turns(1,1000)
		sleep(0.5)
		"""
		Need codes when direction doesn't change.
		"""

#Stop the motors before exiting.
rightMotor.stop()
leftMotor.stop()		

	
