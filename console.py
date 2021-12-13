"""Modul UI"""
from types import FunctionType
from domain.entities import eveniment, legatura
from service.lista_evenimente import listaEvenimente
from service.lista_persoane import listaPersoane
from service.lista_inscrieri import listaInscrieri
from auxiliaries.randomGenerator import genEvent,genPersoana, genInsc
from auxiliaries.sorters import mergeSort, bingoSort
import random
from datetime import date

def convertData(data):
    data = data.split('/')
    data = date(int(data[2]), int(data[1]), int(data[0]))
    return data

def dateCmp(a:eveniment, b:eveniment):
    #returneaza criteriile de comparare pentru evenimente

    dataA = convertData(a.getData())
    dataB = convertData(b.getData())
    
    if dataA == dataB:
        oraA = a.getTimp()
        oraA.split(':')
        
        oraB = b.getTimp()
        oraB.split(':')

        if oraA[0] == oraB[0]:
            return oraA[1] < oraB[1]
        else:
            return oraA[0] < oraB[0]
    
    else:
        return dataA < dataB
        

def descKey(a:eveniment):
    descA = a.getDescriere()

    return len(descA)

class consola:
    
    __events = listaEvenimente()
    __persoane = listaPersoane()
    __inscrieri = listaInscrieri()
    __generator = (genEvent, genPersoana, genInsc)
    
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

        self.__inscrieri.inscriePersoana(pers,int(event))

    def populate(self):
        nEvent = random.randint(1,100)
        nPers = random.randint(1,100)
        nInsc = random.randint(1,1000)
        (gEven, gPers, gInsc) = self.__generator
        for i in range(nEvent):
            (data, timp, descriere) = gEven()
            self.__events.addEveniment(data, timp, descriere)
        
        for i in range(nPers):
            (nume, adresa)= gPers()
            self.__persoane.addPersoana(nume, adresa)

        duplicateCounter = 0
        for i in range(nInsc):
            (idP, idE) = gInsc(nPers, nEvent)
            try:
                self.__inscrieri.inscriePersoana(idP, idE)
            except ValueError as e:
                duplicateCounter +=1

        print("S-au realizat {} inscrieri".format(duplicateCounter))
        print()
        print("Listele au fost populate!")

    def cautaPersoana(self):
        """Cauta persoana cu numele dat
        """
        nume = input("Introdu numele persoanei cautate: ")

        
        res = self.__persoane.searchPers(nume = nume)
        res = self.__persoane.getPIndex(res)
        print(self.__persoane.getPersoana(res))
        
    def cautaEveniment(self):
        """Cauta un eveniment dupa ID

        """
        res = input("Introdu ID-ul evenimentului cautat: ")
        res = int(res)
        res = self.__events.getEveniment(self.__events.getEIndex(res))
        print(res)

    def evenAfisData(self):

        numePers = input("Introdu numele persoanei: ")
        idP = self.__persoane.searchPers(numePers)
        
        inscrieri = self.__inscrieri.getInscrieriPers(idP)
        inscrieri = [self.__events.getEIndex(i) for i in inscrieri]
        inscrieri = [self.__events.getEveniment(i) for i in inscrieri]

        inscrieri = mergeSort(inscrieri, cmp = dateCmp, reverse=False)
        for inst in inscrieri:
            print(inst)

    def persParticipMax(self):
        """Afiseaza persoanele cu cele mai multe participari
        """
        pers = self.__persoane.getAll()
        maxi = 0
        rsp = []
        for p in pers:
            insc = self.__inscrieri.getInscrieriPers(p.getID())
            if maxi < len(insc):
                maxi = len(insc)
                rsp.clear()
                rsp.append(p)
            elif maxi == len(insc):
                rsp.append(p)
        
        for pers in rsp:
            print(pers)
            print("Nr inscrieri: {}".format(maxi))
            print("*"*10)
        
        


    def evenAfisDesc(self):

        numePers = input("Introdu numele persoanei: ")
        idP = self.__persoane.searchPers(numePers)
        
        inscrieri = self.__inscrieri.getInscrieriPers(idP)
        inscrieri = [self.__events.getEIndex(i) for i in inscrieri]
        inscrieri = [self.__events.getEveniment(i) for i in inscrieri]

        inscrieri = mergeSort(inscrieri, key=descKey, reverse=True)

        for inst in inscrieri:
            print(inst)

    def top20(self):
        ans = self.__inscrieri.topEvenim()
        for p in ans:
            pos = self.__events.getEIndex(p)
            print(self.__events.getEveniment(pos))
            print(ans[p])



    def getComenzi(self):
        comenzi = {"Afisează toate persoanele.":self.showPersoane,
               "Afisează toate evenimentele.":self.showEvenimente,
               "Afisează persoanele cu cele mai multe inscrieri":self.persParticipMax,
               "Populează listele":self.populate,
               "Adaugă persoană.":self.addPersoana,
               "Adaugă eveniment.":self.addEveniment,
               "Caută persoană.":self.cautaPersoana,
               "Caută eveniment.":self.cautaEveniment,
               "Afiseaza evenimentele persoanei sortate dupa data.":self.evenAfisData,
               "Afiseaza evenimentele persoanei sortate dupa descriere.":self.evenAfisDesc,
               "Înscrie o persoană la un eveniment.":self.inscriePersoana,
               "Top 20% evenimente cu cele mai multe inscrieri.":self.top20,
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

            



    
