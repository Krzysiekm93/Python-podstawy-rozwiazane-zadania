h = int(input("Podaj wysokosc choinki: "))

for i in range(0, h):
    print((("*" + ("*" * (i * 2))).center(h*2)))