import turtle as t
def draw_circle(x,y,radius1):
    t.penup()
    t.goto(x,y - radius1) 
    t.pencolor("black")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(radius1)
    t.end_fill()

def draw_centered_circle(x,y,radius2):
    t.penup()
    t.goto(x,y-radius2) 
    t.fillcolor("brown")
    t.begin_fill()
    t.circle(radius2)
    t.end_fill()

def cursor_to_the_centre():
    t.penup()
    t.goto(x,y) 


def main():
    cor_1 = int(input("Enter the x coordinate : "))
    cor_2 = int(input("Enter the y coordinate : "))
    radius1 = int(input("Enter the radius : "))
    radius2 = int(input("Enter the radius for second circle: "))
    circle = draw_circle(cor_1,cor_2,radius1)
    print(circle)
    circle2 = draw_centered_circle(cor_1,cor_2,radius2)
    print(circle2)
    cursor_to_the_centre()
    input()
main()
