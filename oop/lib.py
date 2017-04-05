#user/bin/env python3

"""import modules"""
from time import sleep
from ev3dev.ev3 import *
import threading
import sys, os  #useless import


"""define the classes of component"""
class Motor:

    def initial(self):
        self.rightMotor = LargeMotor(OUTPUT_B)
        self.leftMotor  = LargeMotor(OUTPUT_C)
        # self.tailMotor  = LargeMotor(OUTPUT_A)

        self.found=0
    def move(self,leftSpeed=1000,rightSpeed=1000,tailSpeed=1000):
        #basic function to control motors
        self.leftMotor.run_forever(speed_sp=leftSpeed)
        self.rightMotor.run_forever(speed_sp=rightSpeed)
        # self.tailMotor.run_forever(speed_sp=-tailSpeed)
    def straightMove(self,inputSpeed=1000):
        #accelerate when approaching near, then input 1000 to get this function
        self.move(inputSpeed,inputSpeed)
    def turnsAngle(self,angle,inputSpeed=1000):
        """this funciton is for turning a certain angle"""
        #dir==1 is right turn, angle > 0 is right turn
        if angle>0:
            dir=1
        else:
            dir=-1
        # self.tailMotor.run_forever(speed_sp=0)
        self.leftMotor.run_timed(speed_sp=dir*inputSpeed,time_sp=angle)
        self.rightMotor.run_timed(speed_sp=-dir*inputSpeed,time_sp=angle)

    def turns(self,dir,inputSpeed=1000):
        #dir==1 is right turn
        self.move(dir*inputSpeed,-dir*inputSpeed,500)

    def break0(self):
        #to stop the motors
        self.leftMotor.stop()
        self.rightMotor.stop()
        # self.tailMotor.stop(stop_command='brake')
        # to make extra sure the motors have stopped:
        self.move(0,0)

    def reverse(self):
        #move backward at full speed.
        self.move(-1000,-1000)
    def findEnemy():
        if self.found==0:
            self.turns(1)
        if self.found!=0:
            self.turnsAngle(self.found*1000)
            sleep(1)
            self.turnsAngle(self.found*-2000)
            sleep(2)



class Gyro:

    def initial(self):
        self.gs = GyroSensor()
        self.gs.mode = 'GYRO-ANG'	# Changing the mode resets the gyro
        self.gs.mode = 'GYRO-RATE'	# Set gyro mode to return compass angle
    def reset(self):
        self.gs.mode = 'GYRO-ANG'
        self.gs.mode = 'GYRO-RATE'
    def isEnemy(self):
        self.reset()
        if (self.gs.value() > -10 and self.gs.value() < 10):
            return 1
        return 0
class Color:
    def initial(self):
        self.cs = ColorSensor();
        self.cs.mode = 'COL-COLOR' 	#set the color sensor to the COLOR mode
    def isEdge(self):
    	if self.cs.value == 1:
    		return 1
    	return 0
class Sonar:

    def initial(self):
        #initial the object and set the initialDistance
        self.us  = UltrasonicSensor()
        self.initialDistance = self.distance()
    def distance(self):
        #return the Sonar sensor's value
        return self.us.value()
    def isEnemy(self):
        # judge if there is enermy
        if self.distance()<(self.initialDistance-100):
            # some object in the maxidistance
            raise EnemyFound()
        return 0
class Touch:
    def initial(self):
        self.ts =  TouchSensor(INPUT_1)
    def touch_isEnemy(self):
        # something push the back
        if self.ts.value():
            return 1


class initialThread(threading.Thread):
    # thread for initialising
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print ("Start initialising")
        threadLock.acquire()
        initFun()
        threadLock.release()
        print("Finished initialisation")




#expection classes
class ButtonPress(Exception):
	def __init__(self, message):
		self.message = message

class EnemyFound(Exception):
	def __init__(self, found=1000):
		self.value = found

class SidesEnemy(Exception):
	def __init__(self, side):
		self.value = side

class DetectRing(Exception):
	def __init__(self, backforwards):
		self.value = backforwards

"""initial the var type for component"""
motor =Motor()
gyro  =Gyro()
color =Color()
sonar =Sonar()
touch =Touch()

btn=Button()
"""initial threadLock for safety threading"""
threadLock=threading.Lock()
"""initialisation function"""
def initFun():
    #initial the object and connect to the component
    motor.initial()
    gyro.initial()
    color.initial()
    sonar.initial()
    touch.initial()
def expectionSleep(duration):

    while duration>0:
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
