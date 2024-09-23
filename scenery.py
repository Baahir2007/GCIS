'''
Baahir's Repository link - https://github.com/Baahir2007/GCIS.git
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

import turtle as t

def table_leg(th,tc):

    '''A function designed to create 
    the leg piece of a table'''
    
    t.down()
    t.fillcolor(tc)
    t.begin_fill()
    t.forward(th)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(th)
    t.left(90)
    t.forward(10)
    t.end_fill()
    t.up()

def table(tw,tc):

    '''function to create the 2d 
    table with 4 legs'''

#This portion of code is to create the table top

    strt = tw//2

    t.fillcolor(tc)
    t.begin_fill()
    t.up()
    t.goto(-(strt),0)
    t.down()
    t.forward(tw)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(tw)
    t.right(90)
    t.forward(10)
    t.end_fill()
    
#This is the portion of code dedicated to creating the legs of the table
    
    tll = float(input("Enter the length of the legs: ")) # asking the user for their preferences
    tlc = input("Enter the color of the legs: ") # asking the user for their preferences

    t.up()
    t.goto(-(strt-10),-10)
    t.right(180)
    table_leg(tll,tlc)
    t.goto(-40,-10)
    t.left(90)
    table_leg(tll,tlc)
    t.goto(30,-10)
    t.left(90)
    table_leg(tll,tlc)
    t.goto((strt-20),-10)
    t.left(90)
    table_leg(tll,tlc)


def cakedetails(): # here we are asking the user for their preferences so they can customize their cake
    cw = float(input("Enter a width for the layers (less than table width): "))
    ch1 = float(input("Enter 1st layer height: "))
    cc1 = input("Enter 1st layer color: ")
    ch2 = float(input("Enter 2nd layer height: "))
    cc2 = input("Enter 2nd layer color: ")
    ch3 = float(input("Enter 3rd layer height: "))
    cc3 = input("Enter 3rd layer color: ")
    return cw,ch1,ch2,ch3,cc1,cc2,cc3 # here we are returning the variables so we can use them later
    
def cakelayers(cw,ch,cc,height): # here is how each cake layer is created
    t.penup()
    t.goto(-cw//2,height) # we are making it negative and dividing by two to allow the cake layers to be centered on the table
    t.fillcolor(cc)
    t.begin_fill()
    t.pendown()
    t.forward(ch)
    t.right(90)
    t.forward(cw)
    t.right(90)
    t.forward(ch)
    t.right(90)
    t.right(90)
    t.end_fill()
    
def decoration1(cw,height): # this makes four white semi-circles on the top layer for decoration
    t.penup()
    t.goto(-cw//2,height) 
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.setheading(270)
    t.circle(cw/8,180) # we are dividing by 8 so each semi-circle fits with the width of the cake
    t.setheading(270)
    t.circle(cw/8,180)
    t.setheading(270)
    t.circle(cw/8,180)
    t.setheading(270)
    t.circle(cw/8,180)
    t.end_fill()

def candle(height):
    
    '''The function to create a candle 
    on top of the cake'''
    t.up()
    t.goto(-2.5,height-10)
    t.down()
    t.begin_fill()
    t.forward(15)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(5)
    t.fillcolor('dark red')
    t.end_fill()
    t.up()
    t.goto(0,height-10)
    t.right(90)
    t.forward(15)
    t.down()
    t.pencolor('yellow')
    t.forward(5)
    t.up()
    t.goto(100,100)

def main():
    t.bgcolor("skyblue") # this is to make the background color skyblue
    t.speed(0) # this is so the drawing gets completed quickly

    tw = float(input("Enter the width of the table(100-300):  ")) # asking the user for their preferences
    tc = input("Enter the color of the table: ") # asking the user for their preferences
    table(tw,tc)

    cw,ch1,ch2,ch3,cc1,cc2,cc3 = cakedetails() # this is were the return function is being used for 
    t.speed(1)
    if cw > tw: # here if the cake width is larger than the table width it will print that and turtle will crash
        print("Cake is too big!!")
        return
    else:
        print("Preparing Cake!!") # if it isnt it will print this and continue with the rest of the code
        t.right(90)
        height = 0  # this is so the cake can start on top of the table top
        cakelayers(cw,ch1,cc1,height)
        height += ch1 # this is to assign a new value to the same variable
        
        cakelayers(cw,ch2,cc2,height)
        height += ch2
        
        cakelayers(cw,ch3,cc3,height)
        height += ch3
        
        decoration1(cw,height)
        height += 10
        
        candle(height)

        print("Happy Birthday!!")
    
    input("Enter to exit... ") # the user can exit whenever they want

main()
