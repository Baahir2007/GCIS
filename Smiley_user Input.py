import turtle as t

def Centered_Circle(x_center,y_center,radius,circle_color):
    t.penup()
    t.goto(x_center, y_center -radius)
    t.pendown()
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def smiley_face(x_center,y_center,head_radius,head_color):
    print(Centered_Circle(x_center,y_center,head_radius,head_color))

def smiley_nose(x_center,y_center,nose_radius,nose_color):
    print(Centered_Circle(x_center,y_center,nose_radius,nose_color))

def smiley_eyes(x_center,y_center,head_radius,eye_radius,Iris_color):
    #Right eye
    Centered_Circle(x_center + 0.25*head_radius,y_center + 0.35*head_radius,eye_radius,"White")
    Centered_Circle(x_center + 0.25*head_radius,y_center + 0.35*head_radius,eye_radius/2,Iris_color)
    Centered_Circle(x_center + 0.25*head_radius,y_center + 0.35*head_radius,eye_radius/4,"Black")
    #Left eye
    Centered_Circle(x_center - 0.25*head_radius,y_center + 0.35*head_radius,eye_radius,"White")
    Centered_Circle(x_center - 0.25*head_radius,y_center + 0.35*head_radius,eye_radius/2,Iris_color)
    Centered_Circle(x_center - 0.25*head_radius,y_center + 0.35*head_radius,eye_radius/4,"Black")

def smiley_mouth(x_center ,y_center ,mouth_radius , head_radius):
    t.penup()
    t.goto( x_center - 0.6*mouth_radius, y_center - 0.25*mouth_radius)
    t.pendown()
    t.right(90)
    t.fillcolor("Black")
    t.begin_fill()
    t.circle(0.6*head_radius,180)
    t.end_fill()
    t.left(90)
    t.forward(mouth_radius)
    t.setheading(0)




def main():
    x_center = int(input("Enter the x-coordinate of the centre of smiley face : "))
    y_center = int(input("Enter the y-coordinate of the centre of smiley face : "))
    head_radius = int(input("Enter the radius of the head : "))
    head_color = input("Enter Head color: ")
    nose_radius = int(input("Enter the nose radius : "))
    nose_color = input("Enter the nose color : ")
    eye_radius = int(input("Enter the radius of the eye: "))
    Iris_color = input("Enter the Iris color: ")
    mouth_radius = int(input("Enter mouth radius : ")) #100

    print(smiley_face(x_center,y_center,head_radius,head_color))
    print(smiley_nose(x_center,y_center,nose_radius,nose_color))
    print(smiley_eyes(x_center,y_center,head_radius,eye_radius,Iris_color))
    print(smiley_mouth(x_center,y_center,mouth_radius,head_radius))
    input()

main()

