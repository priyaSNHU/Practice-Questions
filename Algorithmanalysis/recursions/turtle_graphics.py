import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, len_text):
    if (len_text >= 0):
        my_turtle.forward(len_text)
        
        my_turtle.left(90)
        
        draw_spiral(my_turtle , len_text -5)

draw_spiral(my_turtle , 100)
my_win.exitonclick()
        
