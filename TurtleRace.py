from turtle import Turtle, Screen
import random

color=["violet","indigo","blue","green", "yellow", "orange","red"]
y_pos=[300,200,100, 0,-100, -200, -300]
    
screen=Screen() #making an object of the class screen
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Turtle Racing!")
user_bet=screen.textinput(title="Place your bets!", prompt=" Who do you think will win?")

def finishLine():
    line=Turtle()
    line.color("white")
    line.hideturtle()
    line.width(20)      
    line.penup()
    line.goto(x=400, y=350)
    line.pendown()
    line.goto(x=400, y=-350)

def race():
    turtles=[]
    for i in range(0,7):
        new_turtle=Turtle("turtle")
        new_turtle.shapesize(2)
        new_turtle.color(color[i])
        new_turtle.penup()
        new_turtle.goto(x=-400, y=y_pos[i])
        turtles.append(new_turtle)

    if user_bet:
        race_is_on=True

    while race_is_on:
        for turtle in turtles:
            if turtle.xcor()>400:
                winner=turtle.pencolor()
                if(winner==user_bet):
                    turtle.write(f"Congratulations, you've WON!! The winner is {winner}", align="right", font=("times new roman", 24, "bold"))
                else:
                    turtle.write(f"You've lost! The winner is {winner}. Better luck next time.", align="right", font=("times new roman", 24, "bold"))
                race_is_on=False
            rand_dist=random.randint(0,20)
            turtle.forward(rand_dist)
        
def main():
    finishLine()
    race()

main()
    
screen.exitonclick()


