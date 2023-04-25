import turtle as tur

tur.bgcolor('black')
tur.speed(80)
tur.hideturtle()

colors = ["white", "salmon", "pink", "red"]

for i in range(120):
    for c in colors:
        tur.color(c)
        tur.circle(180-i, 100)
        tur.lt(90)
        tur.circle(180-i, 100)
        tur.end_fill()
tur.mainloop()
