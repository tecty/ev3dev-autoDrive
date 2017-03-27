
#registrate function
ts = TouchSensor(INPUT_1);	assert ts.connected


def touch_isTouch():
    # something push the back
    if ts.value():
        return 1
