# Contoh Solusi Lab 0 DDP 1 2022/2023 

import turtle

turtle.penup()
turtle.goto(-160,110)

# mengubah warna menjadi biru
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()

# membuat huruf C
turtle.forward(160)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(160)
turtle.right(90)
turtle.forward(200)

turtle.end_fill()

# memindahkan turtle
turtle.penup()
turtle.right(90)
turtle.forward(180)

# mengubah warna menjadi merah
turtle.pendown()
turtle.color('red')
turtle.begin_fill()

# membuat huruf S
turtle.forward(160)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(160)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(120)

turtle.end_fill()

turtle.hideturtle() # menyembunyikan ikon turtlenya
turtle.exitonclick()