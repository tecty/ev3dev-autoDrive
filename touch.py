from ev3dev.ev3 import *

#registrate function
ts = TouchSensor(INPUT_4);	assert ts.connected


def touch_isTouch():
    # something push the back
    if ts.value():
        return 1
