import tkinter as tk
import random as rand
import re

root = tk.Tk()
root.title('Evžen The Snake')
root.iconbitmap('img/Snake_hlava.ico')

c = tk.Canvas(root,bg= '#13262f', width= 800, height= 800)
c.pack()

apple = 0
appleCoords = []

realEvzen = 0
realEvzenTail = []


def mainMenu():
    global imgMenu, menu, playBtn, backBtn

    c.delete('all')
    try:
        retryBtn.destroy()
        backBtn.destroy()
    except:
       pass

    try:
        menuBtn.destroy()
        easyDifBtn.destroy()
        mediumDifBtn.destroy()
        hardDifBtn.destroy()
    except:
        pass


    imgMenu = tk.PhotoImage(file="img/main_menu.png")
    menu = c.create_image(400,400,image=imgMenu,anchor='center')

    playBtn = tk.Button(text='Hrať',command=settingsMenu, padx=76,pady=9,font='sans 15 bold', bg='#2E7E2E', bd=0, fg='white')
    playBtn.place(relx=0.37,rely=0.525)


def settingsMenu():

    global easyDifBtn, mediumDifBtn, hardDifBtn, playBtn, menuBtn, backBtn

    c.delete('all')
    try:
        playBtn.destroy()
        retryBtn.destroy() 
        backBtn.destroy()    
    except:
       pass

    menuBtn = tk.Button(text='Späť',command=mainMenu,bd=0,bg='#12222e',fg='white')
    menuBtn.place(relx=0.025,rely=0.025,relwidth=0.08,relheight=0.025)

    c.create_text(400,200,text='Obtiažnosť', fill='white',font=("Arial", 20))

    easyDifBtn = tk.Button(text='Ľahká',command= lambda: game(320),font='sans 10 bold', bg='#3C9E3C', bd=0, fg='white')
    easyDifBtn.place(relwidth = 0.25 ,relheight= 0.06,relx=0.5,rely=0.4,anchor='center')

    mediumDifBtn = tk.Button(text='Stredná',command= lambda: game(200),font='sans 10 bold', bg='#2E7E2E', bd=0, fg='white')
    mediumDifBtn.place(relwidth = 0.25 ,relheight= 0.06,relx=0.5,rely=0.48,anchor='center')

    hardDifBtn = tk.Button(text='Ťažká',command= lambda: game(80),font='sans 10 bold', bg='#3C9E3C', bd=0, fg='white')
    hardDifBtn.place(relwidth = 0.25 ,relheight= 0.06,relx=0.5,rely=0.56,anchor='center')


    c.create_text(400,600,text='Rekordy', fill='white',font=("Arial", 15))
    c.create_rectangle(240,615,560,617,fill='gray',outline='')

    with open('records.txt', 'r') as records:
        c.create_text(400,650,text= 'Ľahká obtiažnosť: ' + records.readline() , fill='white',font=("Arial", 12))
        c.create_text(400,675,text= 'Stredná obtiažnosť: ' + records.readline() , fill='white',font=("Arial", 12))
        c.create_text(400,700,text= 'Ťažká obtiažnosť: ' + records.readline() , fill='white',font=("Arial", 12))


def gameOver(difficulty ,score):
    global retryBtn, lastDifficulty, backBtn


    

    with open('records.txt', 'r+') as r:

        def highScore(lineNum):
            line = r.readlines()[lineNum - 1]
            prevHighScore = line[len(line) - 3] + line[len(line) - 2]

            text = r.read()
            text = re.sub(prevHighScore, str(score), text)
            r.seek(0)
            r.write(text)
            #r.truncate()


        if(difficulty == 320):
            line = r.readline()
            if(int(line[len(line) - 3] + line[len(line) - 2]) < score):
                c.create_text(400,300,text='!!! NOVÝ REKORD: ' + str(score) + '!!!', fill='white',font=("Arial", 25))
                highScore(1)
            else:
                c.create_text(400,300,text='Skóre: ' + str(score), fill='white',font=("Arial", 20))
        if(difficulty == 200):
            line = r.readline()
            if(int(line[len(line) - 3] + line[len(line) - 2]) < score):
                c.create_text(400,300,text='!!! NOVÝ REKORD: ' + str(score) + '!!!', fill='white',font=("Arial", 25, "bold"))
                highScore(2)
            else:
                c.create_text(400,300,text='Skóre: ' + str(score), fill='white',font=("Arial", 20))
        if(difficulty == 80):
            line = r.readline()
            if(int(line[len(line) - 3] + line[len(line) - 2]) < score):
                c.create_text(400,300,text='!!! NOVÝ REKORD: ' + str(score) + ' !!!', fill='white',font=("Arial", 25))
                highScore(3)
            else:
                c.create_text(400,300,text='Skóre: ' + str(score), fill='white',font=("Arial", 20))

    

    c.create_text(400,400,text='Game over', fill='white',font=("Arial", 70))

    retryBtn = tk.Button(text='Skúsiť znova',command= lambda: game(lastDifficulty), bg='#2E7E2E',fg='white',bd=0,font='sans 10 bold')
    retryBtn.place(rely=0.62,relx=0.7,relwidth=0.2,relheight=0.05,anchor='center')

    backBtn = tk.Button(text='naspäť',command= settingsMenu, bg='#2E7E2E',fg='white',bd=0,font='sans 10 bold')
    backBtn.place(rely=0.62,relx=0.3,relwidth=0.2,relheight=0.05,anchor='center')


def game(difficulty):
    global playBtn, retryBtn, easyDifBtn, mediumDifBtn, hardDifBtn,lastDifficulty

    lastDifficulty = difficulty

    c.delete('all')
    try:
        playBtn.destroy()
        retryBtn.destroy()
        backBtn.destroy()
    except:
        pass

    try:
        menuBtn.destroy()
        easyDifBtn.destroy()
        mediumDifBtn.destroy()
        hardDifBtn.destroy()
    except:
        pass

    #-------grafika--------
    imgHlava1 = tk.PhotoImage(file="img/Snake_hlava.png")
    imgHlava2 = tk.PhotoImage(file="img/Snake_hlava_90.png")
    imgHlava3 = tk.PhotoImage(file="img/Snake_hlava_180.png")
    imgHlava4 = tk.PhotoImage(file="img/Snake_hlava_270.png")

    imgTelo11 = tk.PhotoImage(file="img/Snake_telo1.png")
    imgTelo12 = tk.PhotoImage(file="img/Snake_telo1_90.png")
    imgTelo13 = tk.PhotoImage(file="img/Snake_telo1_180.png")
    imgTelo14 = tk.PhotoImage(file="img/Snake_telo1_270.png")

    #-----meniace sa telo -> grafika-----
    '''imgTelo21 = tk.PhotoImage(file="Snake_telo2.png")
    imgTelo22 = tk.PhotoImage(file="Snake_telo2_90.png")
    imgTelo23 = tk.PhotoImage(file="Snake_telo2_180.png")
    imgTelo24 = tk.PhotoImage(file="Snake_telo2_270.png")'''

    imgJablko = tk.PhotoImage(file="img/Snake_jablko.png")

    class snake:
        xDir = -1
        yDir = 0
        coords = [400,400]
        length = 3
        prevCoords = [[[560,400],[-1],[0]],[[480,400],[-1],[0]],[[400,400], [-1], [0]]]

    evzen = snake()
    

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


    


    def init():
        
        def appleGenerator():
            global apple , appleCoords

            x = rand.choice((0,80,160,240,320,400,480,560,640,720))
            y = rand.choice((0,80,160,240,320,400,480,560,640,720))

            c.delete(apple,appleCoords)
            apple = c.create_image(x,y,image=imgJablko,anchor='nw')
            appleCoords = [x,y]

        appleGenerator()

        def createEvzen():
            global realEvzen
            
            #----telo-----
            for i in range(0,evzen.length):
                crds = evzen.prevCoords[len(evzen.prevCoords) -i -1][0]
                xdir = evzen.prevCoords[len(evzen.prevCoords) -i -1][1]
                ydir = evzen.prevCoords[len(evzen.prevCoords) -i -1][2]
                
                if(xdir == [1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo12, tags='evzenTail')])
                if(xdir == [-1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo14, tags='evzenTail')])
                if(ydir == [1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo13, tags='evzenTail')])
                if(ydir == [-1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo11, tags='evzenTail')])
           
            #-----hlava------
            if(evzen.xDir == 1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava2,anchor='center')
            if(evzen.xDir == -1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava4,anchor='center')
            if(evzen.yDir == 1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava3,anchor='center')
            if(evzen.yDir == -1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava1,anchor='center')

            c.after(1,countDown)
        

        def countDown():
            countD = 0
            for i in range(1,4):
                c.delete(countD)
                countD = c.create_text(400,400,text=i, font=("Ariel", 100) ,fill='white' ,anchor='center')
                c.update()
                c.after(1000)
            c.delete(countD)
            
        createEvzen()

        '''middleFrameCount = 0
        xDirection = evzen.xDir
        yDirection = evzen.yDir'''
        def moveEvzen():
            global realEvzen, appleCoords



            evzen.coords = [evzen.coords[0] + g.cellSize * evzen.xDir, evzen.coords[1] + g.cellSize * evzen.yDir]
            
            c.delete('evzenTail',realEvzen)

            takenSpots = []

            
            for i in range(0,evzen.length):
                crds = evzen.prevCoords[len(evzen.prevCoords) -i -1][0]
                xdir = evzen.prevCoords[len(evzen.prevCoords) -i -1][1]
                ydir = evzen.prevCoords[len(evzen.prevCoords) -i -1][2]

                takenSpots.append(crds)
                
                if(xdir == [1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo12, tags='evzenTail')])
                if(xdir == [-1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo14, tags='evzenTail')])
                if(ydir == [1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo13, tags='evzenTail')])
                if(ydir == [-1]):
                    realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo11, tags='evzenTail')])
                
                #------meniace sa telo------
                '''else:
                    if(xdir == [1]):
                        realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo12, tags='evzenTail')])
                    if(xdir == [-1]):
                        realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo14, tags='evzenTail')])
                    if(ydir == [1]):
                        realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo13, tags='evzenTail')])
                    if(ydir == [-1]):
                        realEvzenTail.append([c.create_image(crds[0] + 40, crds[1] + 40, image=imgTelo11, tags='evzenTail')])'''
            
            contin = True
            for i in takenSpots:
                if(i == evzen.coords):
                    contin = False

                if(i == appleCoords):
                    appleGenerator()
                    evzen.length += 1 #-----asi neviem este som sa nerozhodol----

            #----hlava------
            if(evzen.xDir == 1):
                 realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava2,anchor='center')
            if(evzen.xDir == -1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava4,anchor='center')
            if(evzen.yDir == 1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava3,anchor='center')
            if(evzen.yDir == -1):
                realEvzen = c.create_image(evzen.coords[0] + 40, evzen.coords[1] + 40,image=imgHlava1,anchor='center')


            
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
            
            evzen.prevCoords.append([evzen.coords,[evzen.xDir],[evzen.yDir]])


            c.update()
            if(contin):
                c.after(difficulty, moveEvzen)
            else:
                gameOver(difficulty ,evzen.length)

        


        moveEvzen()


    init()

    root.bind('<Left>', LeftKey)
    root.bind('<Right>', RightKey)
    root.bind('<Up>', UpKey)
    root.bind('<Down>', DownKey)







mainMenu()

root.mainloop()
