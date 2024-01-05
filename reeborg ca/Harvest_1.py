def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
move()
turn_left()
move()
move()
c = 0

while True:
    
    if object_here():
        take()
    elif not object_here():
        c = c + 1
        if is_facing_north():
            turn_right()
            move()
            turn_right()
        else:
            turn_left()
            move()
            turn_left()
    if c > 5:
        done()
    move()
