class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__pensja = pensja

    def get_imie(self):
        return self.__imie

    def get_nazwisko(self):
        return self.__nazwisko

    def get_pensja(self):
        return self.__pensja

    def set_imie(self, imie):
        self.__imie = imie
        print(f'zmieniono imie na {imie}')

    def set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko
        print(f'zmieniono nazwisko na {nazwisko}')

    def set_pensja(self, pensja):
        self.__pensja = pensja
        print(f'zmieniono pensje na {pensja}')



if __name__ == "__main__":

    pracownik1 = Pracownik("Jan", "Kowalski", 1500)
    pracownik2 = Pracownik("Szymon", "Kowalewski", 1300)
    pracownik3 = Pracownik("Michal", "Kowalczuk", 1100)

    pracownik2.set_nazwisko("Zieba")
    print(pracownik2.get_nazwisko())

    pracownik3.set_pensja(2000)
    print(pracownik3.get_pensja())

    print(pracownik1.get_nazwisko())
