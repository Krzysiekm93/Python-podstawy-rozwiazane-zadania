class Student:

    def __init__(self, imie, nazwisko, oceny):
        print("Utworzono studenta!")
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__oceny = oceny

    def get_imie(self):
        return self.__imie

    def get_nazwisko(self):
        return self.__nazwisko

    def get_oceny(self):
        return self.__oceny

    def set_imie(self, imie):
        self.__imie = imie

    def set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def set_oceny(self, oceny):
        self.__oceny = oceny

    def nadpisz_oceny(self, oceny):
        self.set_oceny(oceny)

    def dodaj_ocene(self, ocena):
        self.__oceny.append(ocena)

    def popraw_ocene(self, ocena, index):
        for i in range(len(self.get_oceny())):
            if i == index:
                self.__oceny[i] = ocena

    def usun_ocene(self, index):
        for i in range(len(self.get_oceny())):
            if i == index:
                del self.__oceny[i]


if __name__ == "__main__":
    student1 = Student("Janek", "Kowalewski", [1, 2, 4, 5])
    student2 = Student("Marian", "Klawiatura", [1, 1, 1, 3])
    student3 = Student("Janina", "Mysz", [1, 2, 2, 2])
    print(student1.get_oceny())

    student1.dodaj_ocene(4)

    print(student1.get_oceny())

    student1.nadpisz_oceny([1, 2, 2, 2, 2, 2])

    print(student1.get_oceny())

    student1.popraw_ocene(4, 0)

    print(student1.get_oceny())

    student1.usun_ocene(0)

    print(student1.get_oceny())

    student1.usun_ocene(0)

    print(student1.get_oceny())