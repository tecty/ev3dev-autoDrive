"""import the lib that all main program need"""
from lib import *
class mainThread(threading.Thread):
    # main programming in this thread
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #main programming must hold 3 sec while initialisation
        print ("Start main thread and hold 3 sec")
        sleep(3)
        # start the main programme, run the robot until a button is pressed
        while not btn.any():
            if not sonar.isEnemy()
        		sonar.reset()
        		motor.turns(dir,inputSpeed) #rotate to find the enemy
        		if gyro.isEnemy():
        			motor.break0()
        			sleep(0.01)
        			motor.straightMove()

        	else:
        		motor.break0()
        		sleep(0.01)
        		motor.straightMove() #the enemy is in front of the robot

        	if color.isEdge():
                motor.straightMove(-1000)
                sleep(1)

# start mainThread as fast as possible
thread1=mainThread()
thread1.start()
# start initialsing
thread2=initialThread()
thread2.start()
# muti-threading
thread1.join()
thread2.join()

print("End of this round")
