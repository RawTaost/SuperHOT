import math

def isTouchingCharacter(cx, cy, x, y):
    return ((x - cx) ** 2) / (32 ** 2) + ((y - cy) ** 2) / (19 ** 2) <= 1