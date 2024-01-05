def turn_right():
    turn_left()
    turn_left()
    turn_left()

def first_L():
    for _ in range(3):
        move()
    turn_left()
    for _ in range(3):
        move()

def next_L():
    turn_right()
    move()
    turn_right()
    first_L()
    
first_L()
for _ in range(3):
    next_L()
