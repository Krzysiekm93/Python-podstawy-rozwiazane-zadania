a = input("Podaj elementy listy po przecinku: ")

myList = a.split(', ')

my_counter = 0
for element in myList:
    if element == '4':
        my_counter += 1

print("Number 4 in the list you provided exists {} times".format(my_counter))