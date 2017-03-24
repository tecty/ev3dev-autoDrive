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
