from tkinter import *
import time
from turtle import width

width = 500
height = 500
xVel = 3
yVel = 2
window = Tk()

canvas = Canvas(window,width=width, height=height)
canvas.pack()
b_photo = PhotoImage(file='code_7.png')
b_image = canvas.create_image(0,0,image=b_photo,anchor=NW)
photo = PhotoImage(file='card_1.png')
m_image = canvas.create_image(0,0,image=photo,anchor=NW)


img_w = photo.width()
img_h = photo.height()
while True:
    coordinates = canvas.coords(m_image)
    print(coordinates)
    if(coordinates[0]>=width - img_w or coordinates[0]< 0):
        xVel = -xVel
    if(coordinates[1]>=width - img_h or coordinates[1]< 0):
        yVel = -yVel
    canvas.move(m_image,xVel,yVel)
    window.update()
    time.sleep(0.01)
window.mainloop()
