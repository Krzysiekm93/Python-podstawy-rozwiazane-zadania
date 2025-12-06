a = input("podaj ciag znakow: ")

def charactersCounter(input):
    inputlength = len(input)
    lettersCounter = 0
    numbersCounter = 0

    for i in range(0, inputlength):
        if input[i].isdigit():
            numbersCounter += 1
        elif input[i].isalpha():
            lettersCounter += 1
        else:
            i+=1
        
    return print("LITERY {}\nCYFRY  {}".format(lettersCounter, numbersCounter))

charactersCounter(a)
