#this this part of code for motors

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)


def motor_directMove(inputSpeed=1000):
    #accelerate when approaching near, then input 1000 to get this function
    leftMotor.run_forever(inputSpeed)
    rightMotor.run_forever(inputSpeed)


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
    leftMotor.run_forever(speed_sp=dir*inputSpeed)
    rightMotor.run_forever(speed_sp=-dir*inputSpeed)

def motor_break():
    #to stop the motor
    leftMotor.stop()
    rightMotor.stop()
    # to make extra sure the motors have stopped:
    leftMotor.run_forever(speed_sp=0)
    rightMotor.run_forever(speed_sp=0)


def motor_reverse():
    #run at full speed.
    motor_accelerate(-1000);
