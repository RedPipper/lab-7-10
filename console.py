"""Modul UI"""
from types import FunctionType
from repository.entities import eveniment
from controller.lista_evenimente import listaEvenimente
from controller.lista_persoane import listaPersoane
from controller.lista_inscrieri import listaInscrieri
from randomGenerator import genEvent,genPersoana
import random


class consola:
    
    __events = listaEvenimente()
    __persoane = listaPersoane()
    __inscrieri = listaInscrieri()
    __generator = (genEvent, genPersoana)

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
    
    def inscriePersoana(self):
        self.showPersoane()
        print('\n')
        pers = input("Introdu numele persoanei alese ")
        pers = self.__persoane.searchPers(nume = pers)

        self.showEvenimente()
        print('\n')
        event = input("Introdu numărul evenimentului ales")

        self.__inscrieri.inscriePersoana(pers,event)

    def populate(self):
        nEvent = random.randint(1,100)
        nPers = random.randint(1,100)
        (gEven, gPers) = self.__generator
        for i in range(nEvent):
            (data, timp, descriere) = gEven()
            self.__events.addEveniment(data, timp, descriere)
        
        for i in range(nPers):
            (nume, adresa)= gPers()
            self.__persoane.addPersoana(nume, adresa)

        print("Listele au fost populate!")

    def getComenzi(self):
        comenzi = {"Afisează toate persoanele.":self.showPersoane,
               "Afisează toate evenimentele.":self.showEvenimente,
               "Populează listele":self.populate,
               "Adaugă persoană.":self.addPersoana,
               "Adaugă eveniment.":self.addEveniment,
               "Caută persoană":None,
               "Caută eveniment":None,
               "Înscrie o persoană la un eveniment.":self.inscriePersoana,
               "Închide aplicația.":self.exit}

        return comenzi

    def getComanda(self, index):
        comenzi = self.getComenzi()
        
        keys = list(comenzi.keys())
        
        return comenzi[keys[index-1]]
        
        

    def start(self):
        while True:
            print("Comenzile posibile sunt: ")
            comenzi = self.getComenzi()
            for i, comanda in enumerate(comenzi.keys()):    
                print(str(i+1) + '.' + comanda)
            
            choice = input("Introdu numărul comenzii alese: ")
            result = self.getComanda(int(choice))
            print('_'*10)
            result()
            print('_'*10)

            



    
