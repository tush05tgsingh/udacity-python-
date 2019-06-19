import turtle

def draw_square(brad):
    for i in range(1,5):
       brad.forward(100)
       brad.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,40):
        draw_square(brad)
        brad.left(10)
 
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(10)

    window.exitonclick()

draw_art()    
