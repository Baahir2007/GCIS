import turtle as t
def Draw_circle(x,y,radius,color):
    t.penup()
    t.goto(x , y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def Draw_nose(x,y,radius,color):
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def Draw_eye(x,y,radius,color1,color2,color3):
    #Cornea
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.fillcolor(color1)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    #Iris
    t.penup()
    t.goto(x,y-(radius/2))
    t.pendown()
    t.fillcolor(color2)
    t.begin_fill()
    t.circle(radius/2)
    t.end_fill()
    #Pupil
    t.penup()
    t.goto(x,y-(radius/4))
    t.pendown()
    t.fillcolor(color3)
    t.begin_fill()
    t.circle(radius/4)
    t.end_fill()

def Draw_mouth(radius,color):
    t.penup()
    t.goto(-radius,-20)
    t.pendown()
    t.right(90)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius,180)
    t.end_fill()
    t.left(90)
    t.forward(radius)
    t.setheading(0)






def main():
    print(Draw_circle(0,0,100,"yellow"))
    print(Draw_nose(0,0,10,"Brown"))
    print(Draw_eye(25,35,20,"white","Brown","black"))
    print(Draw_eye(-25,35,20,"white","Brown","black"))
    print(Draw_mouth(50,"Black"))
    input()
main()
