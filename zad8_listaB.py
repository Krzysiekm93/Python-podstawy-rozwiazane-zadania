x = int(input("podaj wartosc x: "))
y = int(input("podaj wartosc y: "))

def calculate(a, b):
    z = (a+b)*(a+b)
    return z

result = calculate(x,y)
print("({} + {}) ^ 2) = {}".format(x,y,result))
