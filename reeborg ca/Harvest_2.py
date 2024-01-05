def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
move()
turn_left()
move()

y = 0
z = 0

while True:
    
    y = y + 1
    z = z + 1
    
    while object_here():
        take()
    
    move()
    
    if y > 6:
        if is_facing_north():
            turn_right()
            move()
            turn_right()
        else:
            turn_left()
            move()
            turn_left()
        y = 0
        
    if z > 42:
        done()
