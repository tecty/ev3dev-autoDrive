#this part of code for campass

#Connect campass
gs = GyroSensor()
gs.mode = 'GYRO-ANG'	# Changing the mode resets the gyro
gs.mode = 'GYRO-RATE'	# Set gyro mode to return compass angle

def gyro_reset():
    gs.mode = 'GYRO-ANG'
    gs.mode = 'GYRO-RATE'


def gyro_isEnemy():
	gyro_reset()
	while (gs.value() > -10 & gs.value() < 10):
        motor_directMove(1000)
    gyro_reset()
