import turtle

alex = turtle.Turtle()
alex_win = turtle.Screen()

def rec_tur(dist , alex):
    alex.forward(dist)
    alex.left(90)
    alex.forward(dist - 75)
    alex.left(90)
    alex.forward(dist)
    alex.left(90)
    alex.forward(dist - 75)

rec_tur(150, alex)
    
    
