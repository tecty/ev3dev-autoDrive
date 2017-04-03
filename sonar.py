# this file contain the basic funtion for sonnar


us  = UltrasonicSensor();	assert us.connected
# to store the m
initialDistance=0

def sonar_distance():
    return us.value

def sonar_isEnemy():
    # judge if there is enermy
    if initialDistance==0:
        #record the max distance
        initialDistance=sonar_distance()
    else:
        if sonar_distance()<(initialDistance-100):
            # some object in the maxidistance
            return 1
    return 0
