a = (input("Podaj kwoty po przecinku do logow z bankomatu:"))

myList = map(int, a.split(', '))

def generatelogs(list):
    print("ATM logs:")
    for i in list:
        if i < 0:
            i = abs(i)
            print("- {}".format(i))
        elif i > 0:
            print("+ {}".format(i))
        # wykluczenie 0
        else:
            i += 1

def accbalance(list):
    print("ATM balance: ")
    balance = 0
    for element in list:
        balance = balance + element
    return balance

generatelogs(myList)
accbalance(myList)