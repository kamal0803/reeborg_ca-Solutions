def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()
while front_is_clear():
    move()
    if wall_in_front() and not object_here():
        turn_left()
        
    if right_is_clear():
        turn_right()
    
    if object_here():
        done()
