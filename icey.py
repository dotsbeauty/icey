from tkinter import Tk, HIDDEN, NORMAL, Canvas
from tkinter.constants import COMMAND
from typing import NoReturn
from pygame import mixer
mixer.init(44100)
d1 = mixer.Sound("happy.mp3")
d2 = mixer.Sound("toggle.mp3")

def toggle_eyes():
    current_state = c.itemcget(eye_left , 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(eye_left , state = new_state)
    c.itemconfigure(eye_right , state = new_state)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(eye_left , 10,-5)
        c.move(eye_right , -10,-5)
        c.crossed_eyes = True
    else:
        c.move(eye_left , -10,5)
        c.move(eye_right , 10,5)
        c.crossed_eyes = False

def toggle_tongue():
    if not c.tonque_out:
        c.itemconfigure(tongue_tip , state = NORMAL)
        c.itemconfigure(tongue_main , state = NORMAL)
        d2.play()
        c.tonque_out = True
    else:
        c.itemconfigure(tongue_tip , state = HIDDEN)
        c.itemconfigure(tongue_main , state = HIDDEN)
        c.tonque_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

def show_happy(event):
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350):
        c.itemconfigure(cheek_left , state = NORMAL)
        c.itemconfigure(cheek_right , state = NORMAL)
        c.itemconfigure(mouth_happy , state = NORMAL)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        d1.play()
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left , state = HIDDEN)
    c.itemconfigure(cheek_right , state = HIDDEN)
    c.itemconfigure(mouth_happy , state = HIDDEN)
    c.itemconfigure(mouth_normal , state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    return

def sad():
    if c.happy_level == 0 :
        c.itemconfigure(mouth_happy , state = HIDDEN)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad , state = NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)


win= Tk()
win.title('Icey')
c = Canvas(win, width=400, height=400)
c.configure(bg='light blue', highlightthickness=0)
c.body_color = 'white'

ear_left = c.create_oval(85-20,10,85*2-20,90 , outline="black" , fill=c.body_color)
ear_right = c.create_oval(400-(85*2-20),10,400-85+20,90 , outline="black" , fill=c.body_color)

body = c.create_oval(35, 20, 365, 360, outline="black", fill=c.body_color)

eye_left = c.create_oval(140,150,170,180,outline='black' , fill="black", state= NORMAL)
eye_right = c.create_oval(240,150,270,180,outline='black' , fill="black", state=NORMAL)

nose = c.create_oval(200-20,210,200+20,225, outline="black", fill="black")
nose_curve = c.create_line(150,200,200,180,250,200, smooth=1 , width=1 ,state=NORMAL)

mouth_normal = c.create_line(180,250,200,260,220,250, smooth=1 , width=2 ,state=NORMAL)
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(170,250,200,230,230,250,smooth=1 , width=2 , state=HIDDEN)
mouth_angry = c.create_line(170,250,200,230,230,250,smooth=1 , width=2 , state=HIDDEN)

cheek_left = c.create_oval(70,180,120,230,outline='pink' , fill='pink',state=HIDDEN)
cheek_right = c.create_oval(280,180,330,230,outline='lightpink' , fill='pink',state=HIDDEN)

tongue_main = c.create_rectangle(170,250,230,290,outline='black' , fill='black',state=HIDDEN)
tongue_tip = c.create_oval(170,275,230,300,outline='black' , fill='red',state=HIDDEN)

c.pack()

c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind('<Double-1>' , cheeky)

c.crossed_eyes = False
c.tonque_out = False
c.happy_level = 10

win.after(1000,blink)
win.after(5000,sad)
win.mainloop()