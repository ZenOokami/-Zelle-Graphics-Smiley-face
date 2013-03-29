#ZenOokami Code
#Drawing a smiley Face
#Using the Zelle Graphical System 
from graphics import *
import math

#Function for drawing arcs (for the smile)
def Draw_Arc(center_point, radius, start_angle, end_angle, window):
    theta = start_angle
    while(theta < end_angle):
        x_coord = math.sin(theta) * radius + center_point.getX()
        y_coord = math.cos(theta) * radius + center_point.getY()
        point1 = Point(x_coord, y_coord)
        point1.draw(window)
        theta+=0.01

window_title = "I'm Drawing a SMILEY!"
window_width = 600
window_height = 600

my_window = GraphWin(window_title, window_width, window_height)

#Smiley Face
Circle(Point(window_width/2 , window_height/2), 100).draw(my_window)

#Draw Smile using the Draw_Arc function
Draw_Arc(Point(window_width/2, window_height/2), 70, math.pi * -0.5, math.pi * 0.5, my_window)

#Draw Left, then Right Eyes =D
Circle(Point((window_width/2)-30, (window_height/2)- 25), 20).draw(my_window)
Circle(Point((window_width/2)+30, (window_height/2)- 25), 20).draw(my_window)


# And we're done! simply run this program to see your smiley face. Feel free to edit and play
# around with the program to test things out. If this helped you, please let me know and remember
# to support EoZ by liking and sharing our programming videos over at www.youtube.com/essenceofzen
