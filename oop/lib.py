# initial the var type
motor =Motor()
gyro  =Gyro()


def initFun():
    #initial the object and connect to the component
    motor.initial()
    gyro.initial()


class Motor:
    def initial(self):
        self.rightMotor = LargeMotor(OUTPUT_B)
        self.leftMotor  = LargeMotor(OUTPUT_C)
        self.tailMotor  = LargeMotor(OUTPUT_A)
    def move(self,leftSpeed=1000,rightSpeed=1000,tailSpeed=1000):
        #basic function to control motors
        self.leftMotor.run_forever(speed_sp=leftSpeed)
        self.rightMotor.run_forever(speed_sp=rightSpeed)
        self.tailMotor.run_forever(speed_sp=tailSpeed)
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
        self.leftMotor.run_timed(speed_sp=dir*inputSpeed,time_sp=angle)
        self.rightMotor.run_timed(speed_sp=-dir*inputSpeed,time_sp=angle)

    def turns(self,dir,inputSpeed=1000):
        #dir==1 is right turn
        self.move(dir*inputSpeed,-dir*inputSpeed,0)

    def break0(self):
        #to stop the motors
        self.leftMotor.stop()
        self.rightMotor.stop()
        self.tailMotor.stop()
        # to make extra sure the motors have stopped:
        self.move(0,0,0)

    def reverse(self):
        #move backward at full speed.
        self.move(-1000,-1000,-1000)`
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
    	while (self.gs.value() > -10 & gs.value() < 10):
            motor.directMove(1000)
        self.reset()
