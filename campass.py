#this part of code for campass
from ev3dev.ev3 import *

#Connect campass
gs = GyroSensor(INPUT_4)
gs.mode = 'GYRO-ANG'	# Changing the mode resets the gyro
gs.mode = 'GYRO-RATE'	# Set gyro mode to return compass angle

def gyro_reset():
    rightMotor.stop()
    leftMotor.stop()
    sleep(0.1)
    gs.mode = 'GYRO-ANG'
    gs.mode = 'GYRO-RATE'


def gyro_isEnemy():
    gyro_reset()
    if (gs.value() > -10 and gs.value() < 10):
        return 1
    return 0;
