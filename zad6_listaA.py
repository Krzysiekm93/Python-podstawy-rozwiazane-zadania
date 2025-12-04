x = input("Podaj slowo aby dokonac sprawdzenia czy jest palindromem: ")

def isPalindrom(x):
   if x[::1] == x[::-1]:
       return True
   else:
       return False

if isPalindrom(x):
    print("Tak, slowo {} jest palindromem".format(x))
else:
    print("Nie, slowo {} nie jest palindromem".format(x))