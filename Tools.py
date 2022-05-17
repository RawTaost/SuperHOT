import math

def isTouchingCharacter(cx, cy, x, y, a):
    value = (((getDist(cx, cy, x, y) * math.cos(a) - cx) ** 2) / 1024) + (((getDist(cx, cy, x, y) * math.sin(a) - cy) ** 2) / 361)
    test = math.cos(a)
    print(a)
    print(test)
    return value <= 1

def getDist(p1, p2):
    return math.sqrt(((p1[0]- p2[0]) ** 2) + ((p1[1]-p2[1]) ** 2))

def getDist(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))