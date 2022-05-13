import tkinter as tk
import random as rnd
import time
import tkinter.messagebox as tkm


window=tk.Tk()
window.title("Canvas")
window.geometry('650x500')
window.resizable(False,False)
window.configure(bg="grey")

colors=['yellow','green','black','blue','purple']
stop=False
canvas=tk.Canvas(window,width=500,height=500)
canvas.place(x=0,y=0)

circle_count=0
oval_count=0
square_count=0

def draw_circle():
    global circle_count,oval_count,square_count
    color=rnd.choice(colors)
    color_border=rnd.choice(colors)
    d=rnd.randint(1,100)
    x=rnd.randint(0,500-d)
    y=rnd.randint(0,500-d)
    canvas.create_oval(x,y,x + d ,y + d,fill=color,outline=color_border)
    circle_count+=1

def draw_oval():
    global circle_count,oval_count,square_count
    color=rnd.choice(colors)
    color_border=rnd.choice(colors)
    d_1=rnd.randint(1,100)
    d_2=rnd.randint(1,100)
    x=rnd.randint(0,500-d_1)
    y=rnd.randint(0,500-d_2)
    canvas.create_oval(x,y,x + d_1,y + d_2,fill=color,outline=color_border)
    oval_count+=1

def draw_square():
    global circle_count,oval_count,square_count
    color=rnd.choice(colors)
    color_border=rnd.choice(colors)
    d=rnd.randint(1,100)
    x=rnd.randint(0,500-d)
    y=rnd.randint(0,500-d)
    canvas.create_rectangle(x,y,x + d ,y + d,fill=color,outline=color_border)
    square_count+=1
   
def stop_draw():
    global stop
    stop=True

def draw_circles():
    global stop
    global circle_count,oval_count,square_count
    while True:
        draw_circle()
        window.update()
        circle_count+=1
        print(f"circle_count={circle_count}")
        #time.sleep(1)
        if stop:
            stop=False
            break
            

def draw_ovals():
    global stop
    global oval_count,circle_count,square_count
    while True:
        draw_oval()
        window.update()
        oval_count+=1
        print(f"oval_count={oval_count}")
        #time.sleep(1)
        if stop:
            stop=False
            break
            
 
def draw_squares():
    global stop
    global square_count,circle_count,oval_count
    while True:
        draw_square()
        window.update()
        square_count+=1
        print(f"square_count={square_count}")
        #time.sleep(1)
        if stop:
            stop=False
            break
            

def animate_circle():
    global stop
    color=rnd.choice(colors)
    d=rnd.randint(1,100)
    x=rnd.randint(0,500-d)
    y=rnd.randint(0,500-d)
    circle=canvas.create_oval(x,y,x + d ,y + d,fill=color)
    d_x=2
    d_y=2
    while True:
        coords=canvas.coords(circle)
        print(coords)
        left=coords[0]
        right=coords[2]
        top=coords[1]
        bottom=coords[3]
        if left <= 0 or right >= 500:
            d_x=-d_x
        if top <= 0 or bottom >= 500:
            d_y=-d_y
        canvas.move(circle,d_x,d_y)
        time.sleep(0.01)
        window.update()
        if stop:
            stop=False
            break

def stats():
    global oval_count,circle_count,square_count
    print(f"Total= circle_count={circle_count} oval_count={oval_count} square_count={square_count}")

    
circle_button=tk.Button(window,width=15,text="Draw a circle",command=draw_circle)
circle_button.place(x=510,y=20)

oval_button=tk.Button(window,width=15,text="Draw an oval",command=draw_oval)
oval_button.place(x=510,y=60)

square_button=tk.Button(window,width=15,text="Draw a square",command=draw_square)
square_button.place(x=510,y=100)


draw_circles_button=tk.Button(window,width=15,text="Draw Circles",command=draw_circles)
draw_circles_button.place(x=510,y=140)

draw_ovals_button=tk.Button(window,width=15,text="Draw Ovals",command=draw_ovals)
draw_ovals_button.place(x=510,y=180)

draw_squares_button=tk.Button(window,width=15,text="Draw Squares",command=draw_squares)
draw_squares_button.place(x=510,y=220)



stop_button=tk.Button(window,width=15,text="STOP",command=stop_draw,height=8,bg='red')
stop_button.place(x=510,y=340)

stats_button=tk.Button(window,width=15,text="Stats",command=stats)
stats_button.place(x=510,y=300)



animated_circle_button=tk.Button(window,width=15,text="Animated Circle",command=animate_circle)
animated_circle_button.place(x=510,y=260)



























window.mainloop()
