#!/usr/bin/env python3
# to use python3 in ev3
from time import sleep
from ev3dev.ev3 import *
import sys, os
# import all private modules
from motor import *
from color import *
from sonar import *
# from campass import *
from touch import *



# We will need to check EV3 buttons state.
btn = Button()
print("start sleep 3 s")
#sleep(3)
status=0
found=0
while not btn.any():

    # If the robot is being pushed, it will fight back.
    if touch_isTouch():
        if status!=1:
            print("touched",status)
            status=1
            motor_straightMove(-1000)
            statusChanged=1
    # Ultrasonic sensor will find the enemy
    # Measure the distance to the closest object in front of the robot.
    elif sonar_isEnemy():
        if status!=2:
            print("sonnar detected",status)
            status=2
            if us.value()>400:
                motor_turn_opp(-1)
            motor_straightMove()
            statusChanged=1
    elif color_isEdge():
        if status!=3:
            print ("edge detected",status)
            status=3
            statusChanged=1
            motor_shrink_back()
    # elif gyro_isEnemy():
    #     motor_straightMove()
    else:
        if status!=4:
            print ("start detecting enemy",status)
            # The enemy is neither in front of the robot nor at the back.
            motor_turns(1)
            status=4
            statusChanged=1
        """
        Need codes when direction doesn't change.
        """


# Stop the motors before exiting.
rightMotor.stop()
leftMotor.stop()
