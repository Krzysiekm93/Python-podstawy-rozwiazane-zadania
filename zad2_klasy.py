class Pracownik:

    def __init__(self, imie, nazwisko, pensja):
        print("init pracownik")
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

    def set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def set_pensja(self, pensja):
        self.__pensja = pensja


class Informatyk(Pracownik):
    @staticmethod
    def programuj():
        print("programuje...")


class Ksiegowy(Pracownik):
    def policz_roczna_pensje(self, pracownik):
        _miesieczna_pensja = pracownik.get_pensja()
        return _miesieczna_pensja * 12


if __name__ == "__main__":
    ksiegowy1 = Ksiegowy("Jan", "Kowalski", 10000)

    informatyk1 = Informatyk("Krzysztof", "Polko", 400)

    informatyk1.programuj()

    print(ksiegowy1.policz_roczna_pensje(informatyk1))
