def side():
    for _ in range(9):
        if object_here():
            take()
        move()

for _ in range(4):
    side()
    turn_left()
