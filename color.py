#this is the part for the color sensor

# Connect sensors
cs = ColorSensor();					assert cs.connected
cs.mode = 'COL-COLOR' 	#set the color sensor to the COLOR mode

def color_isEdge():
	if cs.value == 1:
		return 1
	return 0