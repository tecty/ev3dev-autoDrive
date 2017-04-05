"""import the lib that all main program need"""
from lib import *
import sys,os
class mainThread(threading.Thread):
    # main programming in this thread
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #main programming must hold 3 sec while initialisation
        print ("Start main thread and hold 3 sec")
        sleep(3)
        while True:

            try:
            # find enemy sonar() return 1
                if(sonar.isEnemy()):
                    raise EnemyFound(1000)

            # get hit from sides
                elif(gyro.isEnemy()):
                    raise SidesEnemy(-1)

            # color sensor detect black color
                if(color.isEdge()):
                    raise DetectRing(-1)

                if btn.any():
                    raise ButtonPress("Stop robot")

                motor.turns(1)

            except EnemyFound as f:
                motor.move()

            except SidesEnemy as s:
                motor.straightMove(-1000)

            except DetectRing as d:
                motor.straightMove(-1000)

            except ButtonPress:
                motor.break0()
                sys.exit()


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
