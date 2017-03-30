#this this part of code for motors

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)
assMotor   = LargeMotor(OUTPUT_A)


def motor_directMove(inputSpeed=1000):
    leftMotor.run_forever(inputSpeed)
    rightMotor.run_forever(inputSpeed)

#accelerate when approaching near
def motor_fullSpeed(inputSpeed=1000):
    leftMotor.run_forever(inputSpeed)
    rightMotor.run_forever(inputSpeed)
    assMotor.run_forever(inputSpeed)

def motor_turnsAngle(dir,inputSpeed=1000):
    #dir==1 is right turn
    assMotor.stop()
    leftMotor.run_timed(speed_sp=dir*inputSpeed,time_sp=188)
    rightMotor.run_timed(speed_sp=-dir*inputSpeed,time_sp=188)
    # Wait until both motors are stopped:
    while any(m.state for m in (leftMotor, rightMotor)):
        sleep(0.1)

def motor_turns(dir,inputSpeed=1000):
    #dir==1 is right turn
    assMotor.stop()
    leftMotor.run_forever(speed_sp=dir*inputSpeed)
    rightMotor.run_forever(speed_sp=-dir*inputSpeed)
    # Wait until both motors are stopped:
    while any(m.state for m in (leftMotor, rightMotor)):
        sleep(0.1)


def motor_break():
    #to stop the motor
    assMotor.stop()
    leftMotor.stop()
    rightMotor.stop()
    # to make extra sure the motors have stopped:
    leftMotor.run_forever(speed_sp=0)
    rightMotor.run_forever(speed_sp=0)


def motor_reverse():
    #run at full speed.
    motor_accelerate(-1000);
