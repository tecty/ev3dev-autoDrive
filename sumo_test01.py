#!/usr/bin/env python3
# to use python3 in ev3

from time import sleep
import sys, os

from ev3dev.ev3 import *

# Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor = LargeMotor(OUTPUT_C)

# Connect touch sensors.
ts = TouchSensor(); assert ts.connected
us = UltrasonicSensor();	assert us.connected
#gs = GyroSensor();		assert gs.connected
#cl = ColorSensor(); assert cl.connected

#cl.mode = 'COL-REFLECT' # Put the color sensor into COL-REFLECT mode to measure reflected light intensity.

#gs.mode = 'GYRO-RATE'	# Changing the mode resets the gyro
#gs.mode = 'GYRO-ANG'	# Set gyro mode to return compass angle

us.mode = 'US-DIST-CM' # Put the US sensor into distance mode.

# We will need to check EV3 buttons state.
btn = Button()
print("1")

def run_motor(right_speed, left_speed):
    rightMotor.run_timed(speed_sp=right_speed, time_sp=30)
    leftMotor.run_timed(speed_sp=left_speed, time_sp=30)
#    rightMotor.run_timed(speed_sp=-right_speed, time_sp=15000)
#    leftMotor.run_timed(speed_sp=-left_speed, time_sp=15000)

startDistance = 0


def sonar_isEnemy():
    global startDistance
    if startDistance == 0:
        startDistance = us.value()
        print("1", startDistance)
    else:
        if us.value() < (startDistance - 100):
            # some object in the maxidistance
            sleep(0.01)
            print("2", us.value, startDistance)
            return True
    return False

def push_enemy():
    if us.value() < 100:
        run_motor(1000, 1000)
    else:
        run_motor(750, 750)
begin = False
# hold for 3 seconds.


def hold_3sec():
    global begin

    if not begin:
        sleep(3)
        begin = True

hold_3sec()
print("2")
# Run the robot until a button is pressed.
while not btn.any():
    print("3")
    if not sonar_isEnemy():
        run_motor(750, -750)
    else:
        rightMotor.stop(stop_action = 'brake')
        leftMotor.stop(stop_action = 'brake')
        sleep(0.01)
        push_enemy()
#        startDistance = 0
    # If the robot is being pushed, it will fight back.
    if ts.value():
        run_motor(-1000, -1000)

    # Ultrasonic sensor will find the enemy
    # Measure the distance to the closest object in front of the robot.
    """
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
    
    
        Need codes when direction doesn't change.
        """


# Stop the motors before exiting.
rightMotor.stop()
leftMotor.stop()