import tkinter as tk
import random as rand
root = tk.Tk()
root.title('Snake')

c = tk.Canvas(root,bg= '#13262f', width= 800, height= 800)
c.pack()

class snake:
    xDir = -1
    yDir = 0
    coords = [400,400]
    length = 2
    prevCoords = [[400,400,480,480]]

evzen = snake()
realEvzen = 0
realEvzenTail = []

class grid:
    allCells = []
    freeCells = []
    takenCells = []

    cellSize = 80

g = grid()


#---grid----
for i in range(0,800//80):
    c.create_line(i*g.cellSize,0,i*g.cellSize,800, fill= '#12222e')
    c.create_line(0,i*g.cellSize,800,i*g.cellSize, fill= '#12222e')

    for y in range(0,800//80):
        g.allCells.append([i*g.cellSize,y*80])
        g.allCells.append([i*g.cellSize,y*80])


def LeftKey(x):
    evzen.xDir = -1
    evzen.yDir = 0

def RightKey(x):
    evzen.xDir = 1
    evzen.yDir = 0

def UpKey(x):
    evzen.yDir = -1
    evzen.xDir = 0

def DownKey(x):
    evzen.yDir = 1
    evzen.xDir = 0


apple = 0
appleCoords = []

def init():
    global realEvzen, apple, appleCoords, realEvzenTail
    
    def createEvzen():
        global realEvzen
        realEvzen = c.create_rectangle(evzen.coords,evzen.coords[0] + g.cellSize, evzen.coords[1] + g.cellSize, fill= 'green', outline='#12222e')
        evzen.coordsSpan = [evzen.coords[0] + g.cellSize, evzen.coords[1] + g.cellSize]
    createEvzen()

    
    def appleGenerator():
        global apple, appleCoords

        x = rand.choice((0,80,160,240,320,400,480,560,640,720))
        y = rand.choice((0,80,160,240,320,400,480,560,640,720))

        c.delete(apple,appleCoords)
        apple = c.create_rectangle(x,y,x + g.cellSize,y + g.cellSize, fill= 'darkred')
        appleCoords = [x,y]

    appleGenerator()


    


    def moveEvzen():
        global realEvzen, realEvzenTail

        evzen.coords = [evzen.coords[0] + g.cellSize * evzen.xDir, evzen.coords[1] + g.cellSize * evzen.yDir]
        
        c.delete('evzenTail',realEvzen)
        
        crds = 0
        for i in range(0,evzen.length):
            crds = evzen.prevCoords[len(evzen.prevCoords) -i -1]
            #realEvzenTail = c.create_rectangle(crds)
            realEvzenTail.append([c.create_rectangle(crds, fill='#003300',outline='#12222e', tags='evzenTail')])
            #print(crds)

        realEvzen = c.create_rectangle(evzen.coords,evzen.coords[0] + g.cellSize, evzen.coords[1] + g.cellSize, fill= 'darkgreen', outline='#12222e')


        if(evzen.coords[0] == appleCoords[0] and evzen.coords[1] == appleCoords[1]):
            appleGenerator()
            evzen.length += 1

        #---limity---
        if(evzen.coords[0] < 0):
            evzen.coords[0] = 800
        if(evzen.coords[0] > 800):
            evzen.coords[0] = -80
        if(evzen.coords[1] < 0):
            evzen.coords[1] = 800
        if(evzen.coords[1] > 800):
            evzen.coords[1] = -80
        
        evzen.prevCoords.append([evzen.coords[0],evzen.coords[1],evzen.coords[0] + g.cellSize, evzen.coords[1] + g.cellSize])
        


        c.update()
        c.after(200, moveEvzen)   # 75

    moveEvzen()


init()

root.bind('<Left>', LeftKey)
root.bind('<Right>', RightKey)
root.bind('<Up>', UpKey)
root.bind('<Down>', DownKey)



root.mainloop()