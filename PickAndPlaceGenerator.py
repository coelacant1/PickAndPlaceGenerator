from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0.0, 0.0), (113.0, 0.0), (168.0, 91.0), (0.0, 132.0)])
ignoreBL = Polygon([(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)])
ignoreBR = Polygon([(109.0, 0.0), (113.0, 0.0), (113.0, 4.0), (109.0, 4.0)])
ignoreTR = Polygon([(164.0, 87.0), (168.0, 87.0), (168.0, 91.0), (164.0, 91.0)])
ignoreTL = Polygon([(0.0, 128.0), (4.0, 128.0), (4.0, 132.0), (0.0, 132.0)])

coorX = 0.0
coorY = 2.5

margin = 2.0
increment = 3

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

def checkMargin(poly, x, y, margin):
    if not poly.contains(Point(coorX + margin, coorY + margin)):
        return False
    elif not poly.contains(Point(coorX + margin, coorY - margin)):
        return False
    elif not poly.contains(Point(coorX - margin, coorY + margin)):
        return False
    elif not poly.contains(Point(coorX - margin, coorY - margin)):
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


def checkMultiple(x, y, margin):
    value = True

    if not checkMargin(polygon, x, y, margin):
        value = False
    if checkMargin(ignoreBL, x, y, margin):
        value = False
    if checkMargin(ignoreBR, x, y, margin):
        value = False
    if checkMargin(ignoreTR, x, y, margin):
        value = False
    if checkMargin(ignoreTL, x, y, margin):
        value = False

    return value


for y in range(yRangMinConv, yRangMaxConv):

    for x in range(xRangMinConv, xRangMaxConv):
        if checkMultiple(coorX, coorY, margin):
            addLED(x, y, 180.0)

        coorX = coorX + increment

    coorY = coorY + increment

    for x in range(xRangMinConv, xRangMaxConv):
        if checkMultiple(coorX, coorY, margin):
            addLED(x, y, 0.0)

        coorX = coorX - increment

    coorY = coorY + increment
    coorX = coorX - increment

f.close()
