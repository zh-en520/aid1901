import turtle


def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow', \
    'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0], \
            getMid(points[0], points[1]), \
            getMid(points[0], points[2])], \
            degree-1, myTurtle)
        sierpinski([points[1], \
            getMid(points[0], points[1]), \
            getMid(points[1], points[2])], \
            degree-1, myTurtle)
        sierpinski([points[2], \
            getMid(points[2], points[1]), \
            getMid(points[0], points[2])], \
            degree-1, myTurtle)
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()
main()