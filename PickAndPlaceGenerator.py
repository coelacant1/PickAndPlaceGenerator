from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0.0, 0.0), (113.0, 0.0), (168.0, 91.0), (0.0, 132.0)])
ignoreBL = Polygon([(0.0, 0.0), (1.0, 0.0), (1.0, 38.0), (0.0, 38.0)])
ignoreBR = Polygon([(111.0, 0.0), (113.0, 0.0), (113.0, 3.0), (111.0, 3.0)])
ignoreTR = Polygon([(164.0, 87.0), (168.0, 87.0), (168.0, 91.0), (164.0, 91.0)])
ignoreTL = Polygon([(0.0, 128.0), (4.0, 128.0), (4.0, 132.0), (0.0, 132.0)])

coorX = 3.0
coorY = 3.0

margin = 2.5
increment = 4.5

xRangMin = -60
xRangMax = 300
yRangMin = -20
yRangMax = 170

xRangMinConv = int(xRangMin / increment)
xRangMaxConv = int(xRangMax / increment)
yRangMinConv = int(yRangMin / increment)
yRangMaxConv = int(yRangMax / increment)

currentLED = 1

f = open("C:\\TestOutput.csv", "w")

f.write("Altium Designer Pick and Place Locations\n")
f.write("\n")
f.write("========================================================================================================================\n")
f.write("File Design Information:\n")
f.write("\n")
f.write("Date:       27/01/21\n")
f.write("Time:       12:00\n")
f.write("Revision:   Not in VersionControl\n")
f.write("Variant:    No variations\n")
f.write("Units used: mm\n")
f.write("\n")
f.write("""\"Designator\","Comment\","Layer\",\"Center-X(mm)\",\"Center-Y(mm)\",\"Rotation\"""")

def checkIntersects(poly, x, y, margin):
    checkPoly = Polygon([Point(coorX + margin, coorY + margin),
                         Point(coorX + margin, coorY - margin),
                         Point(coorX - margin, coorY + margin),
                         Point(coorX - margin, coorY - margin)])

    return not poly.intersects(checkPoly)

def checkContains(poly, x, y, margin):
    checkPoly = Polygon([Point(coorX + margin, coorY + margin),
                         Point(coorX + margin, coorY - margin),
                         Point(coorX - margin, coorY + margin),
                         Point(coorX - margin, coorY - margin)])

    return not poly.contains(checkPoly)

def addLED(x, y, rotation):
    global currentLED
    output = '"U{}","WS2812B","TopLayer","{:0.2f}","{:0.2f}","{}"'.format(currentLED, coorX, coorY, rotation)
    print(output)
    f.write("\n")
    f.write(output)
    currentLED += 1

def checkMultiple(x, y, margin):
    value = True

    if checkContains(polygon, x, y, margin):
        value = False# = False

    if not checkIntersects(ignoreBL, x, y, margin):
        value = False
        print("Inside BL")
    if not checkIntersects(ignoreBR, x, y, margin):
        value = False
        print("Inside BR")
    if not checkIntersects(ignoreTR, x, y, margin):
        value = False
        print("Inside BR")
    if not checkIntersects(ignoreTL, x, y, margin):
        value = False
        print("Inside TL")

    return value

flip = True

for y in range(yRangMinConv, yRangMaxConv):

    for x in range(xRangMinConv, xRangMaxConv):
        flip = not flip

        coorX = coorX + increment

        if checkMultiple(coorX, coorY, margin):
            if flip:
                addLED(x, y, 90.0)
            else:
                addLED(x, y, 0.0)


    coorY = coorY + increment

    for x in range(xRangMinConv, xRangMaxConv):
        flip = not flip

        coorX = coorX - increment

        if checkMultiple(coorX, coorY, margin):
            if flip:
                addLED(x, y, 180.0)
            else:
                addLED(x, y, 270.0)


    print(coorX)


    flip = not flip

    coorY = coorY + increment
    coorX = coorX - increment

f.close()
