def turn_right():
    turn_left()
    turn_left()
    turn_left()

def height_of_hurdle():
    count = 0
    while wall_on_right():
        count = count + 1
        move()
    return count

def jump():
    turn_left()
    height = height_of_hurdle()
    turn_right()
    move()
    turn_right()
    for _ in range(height):
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
