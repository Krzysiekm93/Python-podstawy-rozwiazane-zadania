x = int(input("Zbadaj czy zadana liczba jest liczba pierwsza: "))

def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i = i + 1
    return True

if isPrime(x):
    print("Tak, to jest liczba pierwsza")
else:
    print("Nie, to nie jest liczba pierwsza")