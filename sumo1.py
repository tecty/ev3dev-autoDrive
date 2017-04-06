#!/usr/bin/env python3
# to use python3 in ev3
from time import sleep
from ev3dev.ev3 import *
import sys, os
# import all private modules
#this this part of code for motors
from time import sleep

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)
# import sensors
gs = GyroSensor(INPUT_4)
us  = UltrasonicSensor(INPUT_1);	assert us.connected
ts = TouchSensor(INPUT_4);	assert ts.connected
cs = ColorSensor(INPUT_3);					assert cs.connected

class ButtonPress(Exception):
	def __init__(self, message="button Pressed"):
		self.message = message

class EnemyFound(Exception):
	def __init__(self, found=1000):
		self.value = found

class SidesEnemy(Exception):
	def __init__(self,side = 1):
        self.value = side

class DetectRing(Exception):
    def __init__(self, backforwards =1):
        self.value = backforwards

def motor_move(leftSpeed=1000,rightSpeed=1000):
    #basic function to control motors
    leftMotor.run_forever(speed_sp=leftSpeed)
    rightMotor.run_forever(speed_sp=rightSpeed)
def motor_straightMove(inputSpeed=1000):
    #accelerate when approaching near, then input 1000 to get this function
    motor_move(inputSpeed,inputSpeed)
def motor_turnsAngle(angle,inputSpeed=1000):
    """this funciton is for turning a certain angle"""
    #dir==1 is right turn, angle > 0 is right turn
    if angle>0:
        dir=1
    else:
        dir=-1
    leftMotor.run_timed(speed_sp=dir*inputSpeed,time_sp=angle)
    rightMotor.run_timed(speed_sp=-dir*inputSpeed,time_sp=angle)
def motor_turns(dir,inputSpeed=500):
    #dir==1 is right turn
    motor_move(dir*inputSpeed,-dir*inputSpeed)
def motor_break():
    #to stop the motor
    leftMotor.stop()
    rightMotor.stop()
    # to make extra sure the motors have stopped:
    motor_move(0,0)
def motor_reverse():
    #move backward at full speed.
    motor_move(-1000,-1000)
def motor_shrink_back( inputSpeed=750):
	#move backward for a limited time.
	leftMotor.run_timed(speed_sp=inputSpeed,time_sp=1000)
	rightMotor.run_timed(speed_sp=inputSpeed,time_sp=1000)
	sleep(1)
def motor_turn_opp(dir, inputSpeed=750):
	#move backward for a limited time.
	leftMotor.run_timed(speed_sp=dir*inputSpeed,time_sp=1000)
	rightMotor.run_timed(speed_sp=-dir*inputSpeed,time_sp=1000)
	sleep(1)
def motor_foundEnemy():
    global found
    gryo_reset()
    if found==0:
        motor_turns(1)
    else
        motor_turns(found)
        expSleep(0.5)
        found =-found
        motor_turns(found)
        expSleep(1)
def expSleep(duration):
    while duration>0:
        try:
            sleep(0.1)
            duration-=0.1
        if btn.any():
            raise ButtonPress()
        if sonar.isEnemy():
            raise EnemyFound(1000)
        if gyro.isEnemy():
            raise SidesEnemy()
        if touch.isEnemy():
            raise EnemyFound(-1000)


#this part of code for campass

#Connect campass
# gs.mode = 'GYRO-ANG'	# Changing the mode resets the gyro
# gs.mode = 'GYRO-RATE'	# Set gyro mode to return compass angle
#
# def gyro_reset():
#     rightMotor.stop()
#     leftMotor.stop()
#     sleep(0.1)
#     gs.mode = 'GYRO-ANG'
#     gs.mode = 'GYRO-RATE'
#
#
# def gyro_isEnemy():
#     gyro_reset()
#     if (gs.value() > -10 and gs.value() < 10):
#         return 1
#     return 0;


# this file contain the basic funtion for sonnar


# to store the m
# initialDistance=500
def sonar_isEnemy():
    # # judge if there is enermy
    # if initialDistance==0:
    #     #record the max distance
    #     initialDistance=sonar_distance()
    # else:
    if (us.value()<400):
        # some object in the maxidistance

        if found =0:
            global found
                found=1
        return 1
    else:
        return 0


#registrate function


def touch_isTouch():
    # something push the back
    if ts.value():
        return 1
#this is the part for the color sensor

# Connect sensors
cs.mode = 'COL-COLOR' 	#set the color sensor to the COLOR mode

def color_isEdge():
    print(cs.value())
    if cs.value() == 1:
        return 1
    return 0

# We will need to check EV3 buttons state.
btn = Button()
print("start sleep 3 s")
#sleep(3)
status=0
found =0
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
