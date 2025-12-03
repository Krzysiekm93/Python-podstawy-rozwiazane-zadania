number = int(input("Oblicz silnie dla liczby: "))

def factorial(number):
    result = 1
    for n in range(1, number + 1):
        result = result * n
    return result

print(factorial(number))