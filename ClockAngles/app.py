
# |11/2(m) - 30h| == 125

def getTimes(angle):
# prints the tuples of the the Hour, Minutes of the time at which the angle between the two hands is the angle argument
    for hour in range(12):
        for minute in range(60):
            # angle between the hands can be either the correct angle or reflex angle. This only useful
            # for angles like 270 and 90 that can be applied either way depending on the problem at hand.
            if abs(5.5*minute - 30*hour) == angle or 360-abs(5.5*minute - 30*hour) == angle:
                print(hour,minute)

getTimes(90)