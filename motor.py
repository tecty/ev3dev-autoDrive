#this this part of code for motors

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)
tailMotor  = LargeMotor(OUTPUT_A)

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

def motor_turns(dir,inputSpeed=1000):
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
	
def motor_shrink_back(inputSpeed=750):
	#move backward for a limited time.
	leftMotor.run_timed(speed_sp=inputSpeed,time_sp=1000)
	rightMotor.run_timed(speed_sp=inputSpeed,time_sp=1000)
	sleep(1)
	
