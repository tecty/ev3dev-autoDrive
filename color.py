from ev3dev.ev3 import *
#this is the part for the color sensor

# Connect sensors
cs = ColorSensor(INPUT_3);					assert cs.connected
cs.mode = 'COL-COLOR' 	#set the color sensor to the COLOR mode

def color_isEdge():
    print(cs.value())
    if cs.value() == 1:
        return 1
    return 0
