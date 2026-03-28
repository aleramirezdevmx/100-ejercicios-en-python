import turtle as t
import random
import colorgram


rgb_colors = []
colors = colorgram.extract('arcoiris.jpg', 30)

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()


tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))  
    tim.forward(40) 

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

