import tkinter as tk

root = tk.Tk()

height = 800
width = 1000
c = tk.Canvas(root, bg='#13262f', height= height, width= width)
c.pack()

snakeCoords = [width/2-10,height/2-10,width/2+10,height/2+10]
snake = c.create_rectangle(snakeCoords,fill='black')


increment = -1

def rightKey(event):
    increment = 1
    print('nieco')
    return increment


    


def pohyb():
    c.delete('all')

    if snakeCoords[0] < 0:
        snakeCoords[0] = width-20
        snakeCoords[2] = width

    snakeCoords[0] += increment
    snakeCoords[2] += increment
    print(snakeCoords)

    #c.move(snake,increment,0)
    c.create_rectangle(snakeCoords,fill= 'black')

    c.update()
    c.after(10, pohyb)

pohyb()

#c.bind('<left>', leftKey)
root.bind('<Right>', rightKey)
#c.bind('<up>', upKey)
#c.bind('<down>', downKey)

root.mainloop(

    

)

