from time import sleep
import sys, os

from ev3dev.auto import *

class ButtonPress(Exception):
	def __init__(self, message):
		self.message = message

class EnemyFound(Exception):
	def __init__(self, found):
		self.value = found

class SidesEnemy(Exception):
	def __init__(self, side):
		self.value = side

class DetectRing(Exception):
	def __init__(self, backforwards):
		self.value = backforwards

btn = Button()


while True:

	try:
		# find enemy sonar() return 1
		if(sonar.isEnemy()):
			raise EnemyFound(1000)

		# get hit from sides
		elif(gyro.isEnemy()):
			raise SidesEnemy(-1)

		# color sensor detect black color
		if(color.isEdge()):
			raise DetectRing(-1)

		if btn.any():
			raise ButtonPress("Stop robot")

		motor.turn(1)

	except EnemyFound as f:
		motor.move()

	except SidesEnemy as s:
		motor.move()

	except DetectRing as d:
		motor.move()

	except ButtonPress:
		motor.stop()
		sys.exit()
