import turtle
import random
import math
from tkinter import * 
from tkinter import messagebox

valid = False
while(not valid):
    bottom = turtle.textinput("Input", "Jumlah batu bata pada lapisan paling bawah: ")
    if (int(bottom) < 0):
        messagebox.showinfo("Too small", "Nilai terkecil yang dibolehkan adalah 1. Mohon coba lagi.") # The alert.
    elif (int(bottom) > 25):
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.") # The alert.
    else:
        valid = True
        bottom = int(bottom)

valid = False
while (not valid):
    top = int(turtle.textinput("Input", "Jumlah batu bata pada lapisan paling atas: "))
    if (int(top) < 0):
        messagebox.showinfo("Too small", "Nilai terkecil yang dibolehkan adalah 1. Mohon coba lagi.") # The alert.
    elif (int(top) > int(top)):
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah "+str(bottom)+". Mohon coba lagi.") # The alert.
    else:
        bottom = int(bottom)
        valid = True

level = bottom-top+1

valid = False
while(not valid):
    width = int(turtle.textinput("Input", "Panjang satu buah batu bata (piksel): "))
    if (int(width) < 0):
        messagebox.showinfo("Too small", "Nilai terkecil yang dibolehkan adalah 10. Mohon coba lagi.") # The alert.
    elif (int(width) > 35):
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 35. Mohon coba lagi.") # The alert.
    else:
        width = int(width)
        valid = True

valid = False
while (not valid):
    height = int(turtle.textinput("Input", "Lebar satu buah batu bata (piksel): "))
    if (int(height) < 0):
        messagebox.showinfo("Too small", "Nilai terkecil yang dibolehkan adalah 10. Mohon coba lagi.") # The alert.
    elif (int(height) > 35):
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.") # The alert.
    else:
        height = int(height)
        valid = True

turtle.title("Candi Warna-Warni")
turtle.speed(1000)
turtle.Screen().bgcolor("green")
y = -(level/2)*height
bb_biasa = 0
bb_ww = 0
for i in range(level):
    x = -(bottom-i)/2*width
    y = y+height
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for j in range(bottom-i):
        if i == 0 or i==level-1 or j == 0 or j == bottom-i-1:
            turtle.color("black","#BC4A3C")
            bb_biasa += 1
        else:
            hexcolor = hex(random.randint(2,2**24-1))[2:]
            while len(hexcolor) < 6:
                hexcolor = "0" + hexcolor
            hexcolor = "#"+hexcolor
            turtle.color("black", hexcolor)
            bb_ww += 1
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()


turtle.penup()
y = -(level/2)*height-2*height
x = 0
turtle.goto(x,y)
turtle.pendown()
turtle.write("Candi warna-warni dengan " + str(bb_biasa+bb_ww) + " batu bata", font=("Verdana", 20, "normal"), align = "center")
turtle.penup()
turtle.hideturtle()
turtle.exitonclick()


    



