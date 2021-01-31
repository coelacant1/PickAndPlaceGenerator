from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0.0, 0.0), (100.0, 0.0), (100.0, 100.0), (0.0, 100.0)])

coorX = 0.0
coorY = 2.5

margin = 2.0
increment = 3.5

xRangMin = -50
xRangMax = 300
yRangMin = 0
yRangMax = 150

xRangMinConv = int(xRangMin / increment)
xRangMaxConv = int(xRangMax / increment)
yRangMinConv = int(yRangMin / increment)
yRangMaxConv = int(yRangMax / increment)

currentLED = 1

f = open("C:\\TestOutput.csv", "w")

f.write("""\"Designator\","Comment\","Layer\",\"Center-X(mm)\",\"Center-Y(mm)\",\"Rotation\"""")

def checkMargin(x, y, margin):
    if not polygon.contains(Point(coorX + margin, coorY + margin)):
        return False
    elif not polygon.contains(Point(coorX + margin, coorY - margin)):
        return False
    elif not polygon.contains(Point(coorX - margin, coorY + margin)):
        return False
    elif not polygon.contains(Point(coorX - margin, coorY - margin)):
        return False
    else:
        return True

def addLED(x, y, rotation):
    global currentLED
    output = '"U{}","WS2812B","TopLayer","{:0.2f}","{:0.2f}","{}"'.format(currentLED, coorX, coorY, rotation)
    print(output)
    f.write("\n")
    f.write(output)
    currentLED += 1


for y in range(yRangMinConv, yRangMaxConv):

    for x in range(xRangMinConv, xRangMaxConv):
        if checkMargin(coorX, coorY, margin):
            addLED(x, y, 180.0)


        coorX = coorX + increment

    coorY = coorY + increment

    for x in range(xRangMinConv, xRangMaxConv):
        if checkMargin(coorX, coorY, margin):
            addLED(x, y, 0.0)

        coorX = coorX - increment

    coorY = coorY + increment
    coorX = coorX - increment

f.close()
