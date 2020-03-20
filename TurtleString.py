#Modified by: Angy Shailyn Vasquez
#Email: angy.vasquez65@myhunter.cuny.edu
#A program that uses command strings to control turtle drawing

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     
commands = input("Please enter a command string: ")

for ch in commands:
    if ch == 'S':            
        tess.stamp()
    elif ch == 'D':          
        tess.dot()
    elif ch == 'B':          
        tess.backward(50)
    elif ch == 'p':          
        tess.color("purple")
    else:                   
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         
