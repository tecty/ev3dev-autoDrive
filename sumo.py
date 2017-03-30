#!/usr/bin/env python3
# to use python3 in ev3

from time import sleep
# import all private modules
from motor,color,sonar,campus,touch import *


import sys, os

from ev3dev.ev3 import *

# Connect motors
rightMotor = LargeMotor(OUTPUT_B)

leftMotor  = LargeMotor(OUTPUT_C)

# Connect touch sensors.
ts = TouchSensor()			assert ts.connected
cs = ColorSensor()			assert cs.connected
us  = UltrasonicSensor()	assert us.connected
gs  = GyroSensor()			assert gs.connected

gs.mode = 'GYRO-ANG'	# Set gyro mode to return compass angle

# We will need to check EV3 buttons state.
btn = Button()

# Run the robot until a button is pressed.
begin = 0

while not btn.any():

    if begin == 0:
        # hold for 3 seconds.
        sleep(3)

    begin = 1
    # If the robot is being pushed, it will fight back.
    if ts.value():

        motor_reverse()

    # Ultrasonic sensor will find the enemy
    # Measure the distance to the closest object in front of the robot.
    distance = us.value()

    if distance < 400:
        # The enemy is in front of the robot.
        motor_directMove(1000)

    elif distance<50:
        # The enemy is close to the robot.
        motor_accelerate(1000)

    else:
        # The enemy is neither in front of the robot nor at the back.
        motor_turns(1,1000)
        """
        Need codes when direction doesn't change.
        """


# Stop the motors before exiting.
rightMotor.stop()
leftMotor.stop()
