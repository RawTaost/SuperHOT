import math

def getDist(p1, p2):
    return math.sqrt(((p1[0]- p2[0]) ** 2) + ((p1[1]-p2[1]) ** 2))

def getDist(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def getShortestAngle(alpha, beta):
    alpha %= math.pi * 2
    beta %= math.pi * 2
    if alpha >= beta:
        op1 = alpha - beta
        op2 = (math.pi * 2) - (alpha - beta)
    else:
        op1 = (math.pi * 2) - (beta - alpha)
        op2 = beta - alpha
    
    if op1 <= op2:
        sign = -1
        angleBetween = op1
    else:
        sign = 1
        angleBetween = op2

    return (angleBetween, sign)