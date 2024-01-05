def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cover_boundries():

    while True:
        while object_here():
            take()
            
        if wall_in_front():
            turn_left()
            break
            
        move()       

def cover_inside():
    while True:
        while object_here():
            take()
        
        if wall_in_front():
            turn_right()
            break
        
        move()
        
cover_boundries()
cover_boundries()
cover_boundries()

move()

turn_left()
cover_inside()
move()
turn_right()
cover_inside()

turn_left()
turn_left()
move()

turn_left()
cover_inside()
move()
turn_right()
cover_inside()

turn_left()
while carries_object():
    toss()

turn_left()
move()
turn_right()
move()
