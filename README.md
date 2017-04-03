# ev3dev-autoDrive

    this project is to let ev3 have basic function on robot sumo
---
# APIs
## Motor.py
### motor_move
    Wrote as a basic function. Move with left wheel and right wheel speed.
### motor_directMove
    move directly, mainly keep a straight line, and move forward.
### motor_turnsAngle
    positive is turning right
    turn in certain angle of ev3
### motor_turns
    positive is turning right
    turning forever is not further instruction
### motor_break
    To fully stop the motor
### motor_reverse
    to moving backward with full speed
##sonar.py
###sonar_distance
    Return the distance that sonar detected
###sonar_isEnemy
    If sonar sensor found an enemy that will return ture.
##campass.py
###gyro_reset
    For resets standard angle
###gyro_isEnemy
    If gyro sensor has detected an enermy, return true.
