from graphics import *

win = GraphWin("window", 500,500)

pt1 = Point (190,70)
pt2 = Point (310,70)

pt3 = Point (125,125)
pt4 = Point (375,125)

pt5 = Point (140,250)
pt6 = Point (360,250)

pt7 = Point (220, 400)
pt8 = Point (280,400)

faceStructure = Polygon(pt1, pt3, pt5, pt7, pt8, pt6, pt4, pt2)
faceStructure.draw(win)


aLine= Line(Point(145,125), Point(210,125))
aLine.draw(win)
bLine= Line(Point(355,125), Point(290,125))
bLine.draw(win)

eyePt= Point(190,190)
cir = Circle(eyePt, 30)
cir.draw(win)
cir.setOutline('blue')
cir.setFill('green')

eyePt2= Point(310,190)
cir2 = Circle(eyePt2, 30)
cir2.draw(win)
cir2.setOutline('blue')
cir2.setFill('green')


noseOne = Point(230,260)
noseTwo = Point(250,290)
noseThree =Point (270,260)
triangle = Polygon(noseOne, noseTwo, noseThree)
triangle.draw(win)

newRec=Rectangle(Point(230,310),Point(270,350))
newRec.setFill('pink')
newRec.draw(win)

message= Text(Point(250,420), "Xiao Yi Lin")
message.setTextColor('blue')
message.setStyle('italic')
message.setSize(18)
message.draw(win)

clickPoint = win.getMouse()
win.close()

