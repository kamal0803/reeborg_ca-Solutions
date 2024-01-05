def turn_right():
    turn_left()
    turn_left()
    turn_left()

def opp_L():
    move()
    turn_left()
    move()
    turn_right()

def normal_L():
    move()
    turn_right()
    move()
    turn_left()

for _ in range(6):
    opp_L()
    normal_L()
