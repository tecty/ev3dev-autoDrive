#this this part of code for motors

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)
def motor_directMove(inputSpeed=1000):
    leftMotor.run_forever(inputSpeed)
    rightMotor.run_forever(inputSpeed)

def motor_turns(dir,inputSpeed =1000):
    #dir==1 is right turn
    leftMotor.run_forever(inputSpeed *dir)
    rightMotor.run_forever(inputSpeed *-dir)


def motor_break():
    #to stop the motor
    leftMotor.stop()
    rightMotor.stop()
    # to make extra sure the motors have stopped:
    leftMotor.run_forever(speed_sp=0)
    rightMotor.run_forever(speed_sp=0)
