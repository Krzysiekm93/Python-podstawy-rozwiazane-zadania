import math
radius = int(input("Podaj promien kola do wyliczenia pola: "))

def circleArea (radius):
    area = math.pi * radius * radius
    return area

print(round(circleArea(radius), 4))