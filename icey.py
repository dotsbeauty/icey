from tkinter import Tk, HIDDEN, NORMAL, Canvas
from typing import NoReturn

win= Tk()
win.title('Icey')
c = Canvas(win, width=400, height=400)
c.configure(bg='light blue', highlightthickness=0)
c.body_color = 'white'

ear_left = c.create_oval(85-20,10,85*2-20,90 , outline="black" , fill=c.body_color)
ear_right = c.create_oval(400-(85*2-20),10,400-85+20,90 , outline="black" , fill=c.body_color)

body = c.create_oval(35, 20, 365, 360, outline="black", fill=c.body_color)

eye_left = c.create_oval(140,150,170,180,outline='black' , fill="black")
eye_right = c.create_oval(240,150,270,180,outline='black' , fill="black")

nose = c.create_oval(200-20,210,200+20,225, outline="black", fill="black")
nose_curve = c.create_line(150,200,200,180,250,200, smooth=1 , width=1 ,state=NORMAL)

mouth_normal = c.create_line(180,250,200,260,220,250, smooth=1 , width=2 ,state=NORMAL)
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(170,250,200,230,230,250,smooth=1 , width=2 , state=HIDDEN)

cheek_left = c.create_oval(70,180,120,230,outline='pink' , fill='pink',state=HIDDEN)
cheek_right = c.create_oval(280,180,330,230,outline='lightpink' , fill='pink',state=HIDDEN)

c.pack()
win.mainloop()