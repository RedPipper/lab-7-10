"""Modul UI"""
from types import FunctionType
from lista_evenimente import listaEvenimente
from lista_persoane import listaPersoane

class consola:
    
    __events = listaEvenimente()
    __persoane = listaPersoane()

    def showPersoane(self):
        """Afiseaza lista de persoane
        """
        lst = self.__persoane.getAll()
        for pers in lst:
            print(pers)

    def showEvenimente(self):
        """Afiseaza lista de evenimente
        """
        lst = self.__events.getAll()
        for event in lst:
            print(event)

    def addPersoana(self):
        """Citeste numele si adresa unei persoane si o adauga in lista

        Returns:
            False: Fals daca nu s-a reusit adaugarea persoanei in lista
        """
        nume = input("Introdu numele: ")
        adresa = input("Introdu adresa: ")

        try:
            self.__persoane.addPersoana(nume, adresa)
        except ValueError as e:
            print(e)
            return False
    
    def addEveniment(self):
        """Citeste de la tastatura data, ora si descrierea unui eveniment si
        il adauga in lista

        Returns:
            False: evenimentul nu a putut fi adaugat in lista
        """

        data = input("Introdu data evenimentului: ")
        timp = input("Introdu ora evenimentului: ")
        descriere = input("Introdu descrierea evenimentului: ")

        try:
            self.__events.addEveniment(data, timp, descriere)
        except ValueError as e:
            print(e)
            return False
    
    def exit(self):
        exit()


    
