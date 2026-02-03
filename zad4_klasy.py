from zad2_klasy import Informatyk
from zad3_klasy import Student

class StudiujacyInformatyk(Student, Informatyk) :
    def __init__(self, imie, nazwisko, oceny, pensja):
        Student.__init__(self, imie ,nazwisko, oceny)
        Informatyk.__init__(self,imie, nazwisko, pensja)

if __name__ == "__main__":

    studiujacyinformatyk1 = StudiujacyInformatyk("Grzegorz", "Brzeczyszczykiewicz", [2,2,3,4,5],3000)
    print(studiujacyinformatyk1.get_pensja())
    studiujacyinformatyk1.programuj()