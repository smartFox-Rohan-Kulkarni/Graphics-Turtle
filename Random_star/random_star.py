import turtle
import random

#retruns a random color name from the list.
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink",
              "AntiqueWhite", "Aqua", "Azure", "BlueViolet", "Chartreuse", "BurlyWood", "Crimson",
              "Cyan", "Gold"]

    random.shuffle(colors)
    return colors[0]

if __name__=="__main__":
    window=turtle.getscreen()

    ninja=turtle.Turtle()
    
    ninja.pensize(10)
    ninja.shape("turtle")
    ninja.speed(100)

    dis=0
    angle=140
    
    for _ in range(32):
        turtle.bgcolor(pick_color())
        for _ in range(8):
            ninja.forward(dis)
            ninja.right(angle)
            dis+=2
        ninja.color(pick_color())

    window.exitonclick()

