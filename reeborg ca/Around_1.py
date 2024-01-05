put()
while front_is_clear():
    move()
    if wall_in_front() and not object_here():
        turn_left()
