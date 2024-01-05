put()
while front_is_clear():
    move()
    if object_here():
        done()
    elif wall_in_front():
        turn_left()
