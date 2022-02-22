import tkinter as tk
import random as rand
root = tk.Tk()

c = tk.Canvas(root,bg= '#13262f', width= 800, height= 800)
c.pack()

class snake:
    xDirection = -1
    yDirection = 0
    increment = 80
    coords = (400,400,400 + increment,400 + increment)
    lenght = 1



evzen = snake()
realEvzen = c.create_rectangle(evzen.coords, fill= 'black')

for i in range(0,800//80):
    c.create_line(i*80,0,i*80,800,fill= '#12222e')
    c.create_line(0,i * 80,800,i * 80,fill = '#12222e')


def LeftKey(x):
    evzen.xDirection = -1
    evzen.yDirection = 0

def RightKey(x):
    evzen.xDirection = 1
    evzen.yDirection = 0

def UpKey(x):
    evzen.yDirection = -1
    evzen.xDirection = 0

def DownKey(x):
    evzen.yDirection = 1
    evzen.xDirection = 0

apple = 0
appleCoords = ()
def appleGenerator():
    global apple, appleCoords

    x = rand.choice((0,80,160,240,320,400,480,560,640,720))
    y = rand.choice((0,80,160,240,320,400,480,560,640,720))

    c.delete(apple,appleCoords)
    apple = c.create_rectangle(x,y,x + evzen.increment,y + evzen.increment, fill= 'darkred')
    appleCoords = (x,y)

appleGenerator()




def changeEvzenCoords(x,y):
    evzen.coords = (x,y,x + evzen.increment,y + evzen.increment)


def pohyb():
    global realEvzen, appleCoords
    xMove = evzen.coords[0] + evzen.increment * evzen.xDirection
    yMove = evzen.coords[1] + evzen.increment * evzen.yDirection
    
    c.delete(realEvzen)
    realEvzen = c.create_rectangle(xMove,yMove,xMove + evzen.increment,yMove + evzen.increment, fill= 'black')
    c.update()
    c.after(500, pohyb)

    evzen.coords = (xMove,yMove,xMove + evzen.increment,yMove + evzen.increment)

    if(evzen.coords[0] == appleCoords[0] and evzen.coords[1] == appleCoords[1]):
        appleGenerator()


    if(evzen.coords[0] == 0):
        changeEvzenCoords(800, evzen.coords[1])

    if(evzen.coords[0] == 800):
        changeEvzenCoords(0, evzen.coords[1])

    if(evzen.coords[1] == 0):
        changeEvzenCoords(evzen.coords[0], 800)

    if(evzen.coords[1] == 800):
        changeEvzenCoords(evzen.coords[0], 0)



pohyb()

root.bind('<Left>', LeftKey)
root.bind('<Right>', RightKey)
root.bind('<Up>', UpKey)
root.bind('<Down>', DownKey)


root.mainloop()