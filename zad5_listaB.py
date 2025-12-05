Kolory = ['czerwony', 'zielony', 'niebieski', 'czarny']

def itemsFromList (list = []):
    firstElement = list[0]
    lastElement = list[len(list) - 1]
    print("First element of the given list is: " + firstElement)
    print("Last element of the given list is: " +lastElement)

itemsFromList(Kolory)
