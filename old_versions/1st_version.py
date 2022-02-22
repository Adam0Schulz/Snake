import tkinter as tk

root = tk.Tk()

height = 1000
width = 1000
c = tk.Canvas(root, bg='gray', height= height, width= width)
c.pack()

#width has to be devidable by size
#size = 6

#for i in range(0, width+1, size):
#    c.create_line(size*i,0,size*i,height,fill='#13222f')
#    c.create_line(0,size*i,width,size*i,fill='#13222f')

main = tk.Frame(root,bg='#13262f', highlightbackground="black", highlightthickness=2)
main.place(relwidth= 0.7, relheight= 0.7, rely= 0.15, relx= 0.15)

mainWidth = width * 0.7
mainHeight = height * 0.7

for i in range(1, 700+1, 70):
    x = 70 * i
    y = (mainHeight / 10) * i
    c.create_line(x,height*0.15,x,height*0.7)
    c.create_line(width*0.15,y,width*0.7,y)


root.mainloop()

