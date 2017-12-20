import turtle


def triangle (dist , tri):
    tri.left(60)
    tri.forward(dist)
    tri.right(120)
    tri.forward(dist)
    tri.right(120)
    tri.forward(dist)
    

def main():
    tri = turtle.Turtle()
    tri_win = turtle.Screen()
    tri.color("green")
    tri.fillcolor("orange")
    triangle(200 , tri)
    tri_win.exitonclick()

main()
