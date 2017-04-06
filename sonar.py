# this file contain the basic funtion for sonnar
from ev3dev.ev3 import *


us  = UltrasonicSensor(INPUT_1);	assert us.connected
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
