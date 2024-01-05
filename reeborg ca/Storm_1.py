def turn_right():
    turn_left()
    turn_left()
    turn_left()

while True:
    
    while object_here():
        take()
    
    if wall_in_front():
        if not at_goal():
            turn_left()
            turn_left()
        else:
            turn_right()
            while carries_object():
                toss()
            done()
    move()
