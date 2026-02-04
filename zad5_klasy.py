class int:
    def __init__(self, value):
        self.value = value
        print("stworzono obiekt z konstruktora klasy int")

class int2(int):
    def ultimate_value(self):
        return 42

if __name__ == "__main__":

    moj_int = int(50)
    moj_int2 = int2(100)

    print(moj_int2.ultimate_value())

