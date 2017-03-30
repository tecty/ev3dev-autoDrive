# this file contain the basic funtion for sonnar


us  = UltrasonicSensor();	assert us.connected
# to store the m
unlimitDistance=0

def sonar_distance():
    return us.value

def sonar_isEnermy():
    # judge if there is enermy
    if unlimitDistance==0:
        #record the max distance
        unlimitDistance=sonar_distance()
    else:
        if sonar_distance()<(unlimitDistance-100):
            # some object in the maxidistance
            return 1
    return 0
