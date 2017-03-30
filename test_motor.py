import motor,test as *

"""
rightMotor at OUTPUT_B
leftMotor at OUTPUT_C

"""
motor_move()
printf("this motor_move\n")
testSleep(3)
motor_break()
printf("break\n")



motor_straightMove()
testSleep(3)
printf("this is motor_straightMove\n")
motor_break()



motor_turns(1)
printf("this is right turn\n")
testSleep(1)

motor_turns(-1)
printf("this is left turn\n")
testSleep(1)
motor_break()


motor_turnsAngle(100)
printf("this has turned angle 100\n")
testSleep(1)



motor_reverse()
printf("this is moving backward with full speed\n")
testSleep(3)
motor_break()
printf("end of test \n")
