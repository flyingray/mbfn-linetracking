def LineTracking22():
    global trackingValues
    trackingValues = Rover.line_tracking()
    if trackingValues == 2 or trackingValues == 5:
        Rover.set_allrgb(Rover.colors(RoverColors.GREEN))
        Rover.move(trackingSpeed)
    elif trackingValues == 4 or trackingValues == 6:
        Rover.set_allrgb(Rover.colors(RoverColors.RED))
        Rover.motor_run_dual(speedSlowSide, speedFastSide)
    elif trackingValues == 1 or trackingValues == 3:
        Rover.set_allrgb(Rover.colors(RoverColors.BLUE))
        Rover.motor_run_dual(speedFastSide, speedSlowSide)
    else:
        Rover.set_allrgb(Rover.show_color(0xff00ff))
        Rover.motor_stop_all(MotorActions.STOP)
trackingValues = 0
speedFastSide = 0
speedSlowSide = 0
trackingSpeed = 0
basic.show_icon(IconNames.HAPPY)
trackingSpeed = 110
speedSlowSide = 25
speedFastSide = 110

def on_forever():
    LineTracking22()
basic.forever(on_forever)
