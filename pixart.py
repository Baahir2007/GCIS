import turtle as t
PIXEL_SIZE = 30
ROWS = 20
COLOUMNS = 20

def pixel_grid(Pixel_Color):
    row = 0 
    t.pencolor("black")
    while row < ROWS :
        t.fillcolor(Pixel_Color)
        t.begin_fill()
        col = 0
        while col< COLOUMNS :
            t.fillcolor(Pixel_Color)
            t.begin_fill()
            for i in range(4):
                t.forward(PIXEL_SIZE)
                t.right(90)
            t.end_fill()
            t.penup()
            t.forward(PIXEL_SIZE)
            t.pendown()
            col += 1
        t.penup()
        t.goto(-300,300 - ((row+1)*PIXEL_SIZE))
        t.pendown()
        row += 1
        t.end_fill()
def main():
    t.penup()
    t.goto(-300,300)
    t.pendown()
    t.speed(0)
    pixel_grid("White")
    t.done()
main()