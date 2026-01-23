a = (input("Podaj kwoty po przecinku do logow z bankomatu:"))

def generate_logs(my_input):
    int_array = list(map(int, my_input.split(",")))
    print("ATM logs:")
    for element in int_array:
        if int(element) < 0:
            print(f"- {abs(element)}")
        elif int(element) > 0:
            print(f"+ {element}")

def acc_balance(my_input):
    array = (my_input.split(","))
    print("ATM balance: ")
    balance = 0
    for element in array:
        balance = balance + int(element)
    return balance

generate_logs(a)
print(acc_balance(a))