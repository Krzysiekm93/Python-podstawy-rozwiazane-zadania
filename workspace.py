x = "madam"
print(x[0])
print(x[len(x)-1])

print(x[::1])
print(x[::-1])

Kolory = [1 , 'zielony', 'niebieski', 'czarny']

lastElement = Kolory[len(Kolory)-1]

print(lastElement)


########Zad 7_B?
a = input("Podaj elementy listy po przecinku: ")

myList = list(map(int, a.split(', ')))

def findmaxvalue(list):
    maxvalue = list[0]
    for element in list:
        if element > maxvalue:
            maxvalue = element
    return maxvalue


for element in myList:
    print(('*' * element).center(findmaxvalue(myList)))

print(Kolory[0])

