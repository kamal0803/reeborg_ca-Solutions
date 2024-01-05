def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()
c = 0
while True:
    
    if wall_in_front():
        turn_left()
        
    if object_here() and c>0:
       done()
        
    if right_is_clear():
        turn_right()
      
    move()
    c = c + 1
