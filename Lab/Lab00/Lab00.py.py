# Restu Ahmad Ar Ridho
# NPM : 2206028951

# Pengenalan Python dan Turtle

import turtle as tur

# mengatur tampilan turtle dan warna background
tur.shape("classic")
tur.bgcolor("yellow")

# mengatur kordinat awal untuk gambar "C"
tur.penup()
tur.goto(-25,-100)

# mengatur warna yang akan ditampilkan pada gambar "C"
tur.color("blue") 
tur.begin_fill() # mengaktifkan mode untuk mengisi interior gambar dengan warna yang dipilih

# membuat gambar "C"
tur.pendown()
tur.right(180)
tur.forward(150)
tur.right(90)
tur.forward(200)
tur.right(90)
tur.forward(150)
tur.right(90)
tur.forward(35)
tur.right(90)
tur.forward(115)
tur.left(90)
tur.forward(130)
tur.left(90)
tur.forward(115)
tur.right(90)
tur.forward(35)
tur.end_fill() # menyelesaikan mode untuk mengisi interior gambar dengan warna yang dipilih

# mengatur kordinat awal untuk gambar "S"
tur.penup()
tur.goto(25,-100)

# mengatur warna yang akan ditampilkan dalam gambar "S"
tur.color("red")
tur.begin_fill() # mengaktifkan mode untuk mengisi interior gambar dengan warna yang dipilih

# membuat gambar "S"
tur.pendown()
tur.left(90)
tur.forward(150)
tur.left(90)
tur.forward(118)
tur.left(90)
tur.forward(115)
tur.right(90)
tur.forward(47)
tur.right(90)
tur.forward(115)
tur.left(90)
tur.forward(35)
tur.left(90)
tur.forward(150)
tur.left(90)
tur.forward(118)
tur.left(90)
tur.forward(115)
tur.right(90)
tur.forward(47)
tur.right(90)
tur.forward(115)
tur.left(90)
tur.forward(35)
tur.end_fill() # menyelesaikan mode untuk mengisi interior gambar dengan warna yang dipilih

# berhenti menggambar dan menyembunyikan ikon turtle
tur.hideturtle()
tur.exitonclick()