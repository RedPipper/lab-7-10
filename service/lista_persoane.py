"""
Modul care contine listele de entitati si operatiile 
care pot fi realizate pe acestea
"""
from repository.persList_frepo import perslist_frepo
from domain.entities import persoana
from validator.validator import validPersoana
import os

class listaPersoane:
    def __init__(self, index = 0, filename="data/perslist.txt"):
        """
        Serviciul pentru administrare a listei de persoane
            
            index (int): punctul de indexare al id-urilor listei
        """
        self.__index = index*1000
        self.__persoane = perslist_frepo(filename)
        self.__valid = validPersoana()

    def getAll(self):
        return self.__persoane.getAll()
    def getSize(self):
        return self.__persoane.size()

    def addPersoana(self, nume, adresa):
        """Verifica si apoi adauga persoana in lista

        Args:
            nume (str): Numele persoanei
            adresa (str): Adresa persoanei

        Raises:
            ValueError: greseala in declararea persoanei
        """
        id = self.__index + self.__persoane.size() + 1

        pers = persoana(id, nume, adresa)
        try: 
            self.__valid.validator(pers)
        except ValueError as e:
            raise ValueError(e)

        lpers = self.__persoane.getAll()
        for p in lpers:
            if p == pers:
                raise ValueError("Persoana există deja în listă.")

        self.__persoane.store(pers)

    def getPIndex(self, IDp):
        """Primeste index-ul catre persoana cu ID-ul cerut

        Args:
            IDp (int): id-ul persoanei cautate

        Returns:
            int: index-ul din lista al obiectului persoana cautat
        """
        lst = self.__persoane.getAll()
        for i, pers in enumerate(lst):
            if pers.getID() == IDp:
                return i
        
        raise ValueError("Persoana nu a fost gasita.")
    
    def getPersoana(self, index):
        """Returneaza obiectul persoana de la index-ul oferit

        Args:
            index (int): index din lista

        Returns:
            persoana: Obiectul persoana de la index
        """
        return self.__persoane.getElem(index)

    def deletePersoana(self, IDp):
        """Sterge persoana cu ID-ul cautat

        Args:
            IDp (int): ID-ul persoanei cautate
        """
        self.__persoane.deleteElem(self.getPIndex(IDp))

    def modifPers(self, IDp, nume=None, adresa=None):
        """Modifica datele persoanei de la ID-ul specificat

        Args:
            IDp (int): ID-ul persoanei cautate
            nume (str, optional): Numele modificat. Defaults to None.
            adresa (str, optional): Adresa modificata. Defaults to None.

        Raises:
            ValueError: Formatul adresei/numelui gresit
        """
        pos = self.getPIndex(IDp)
        pers = self.getPersoana(pos)
        
        #validate section
        valid = persoana(0, nume, adresa)
        try:
            self.__valid.validator(valid)
        except ValueError as e:
            raise ValueError(e)
        
        #modif section
        if nume != None:
            pers.setNume(nume)
        
        if adresa != None:
            pers.setAdresa(adresa)

        allP = self.getAll()
        allP[pos] = pers
        self.__persoane.modifLista(allP)

    def searchPers(self, nume=None, adresa=None):
        """Cauta persoane dupa nume, adresa sau ambele.

        Args:
            nume (str, optional): Numele persoanei cautate. Defaults to None.
            adresa (str, optional): Adresa persoanei cautate. Defaults to None.

        Raises:
            ValueError: Datele introduse sunt gresite

        Returns:
            int: index-ul persoanei



        ###############################ANALIZA COMPLEXITATII#####################################

                Printr-o simpla observare a algoritmului putem determina faptul ca avem, in mare parte, 
            un numar constant de operatii, mai putin apelul functiei "self.getAll()" si structura 
            repetitiva de dupa.
                
                Astfel, determinam ca:
                    1. Prin urmarirea apelului "self.getAll()" observam ca acesta are o complexitate 
                    in timp dependenta de numarul de valori din fisier (posibil si viteza de citire din fisier??).
                        deci la T(n) se adauga numarul de valori din fisier ( T(n) = n ).
                    
                    2. Prin structura repetitiva urmatoare (linia 166) este la fel dependenta de numarul de valori din
                    fisier (in cel mai rau caz), astfel se adauga la T(n) aceeasi valoare 
                    ( rezulta ca in final T(n) = 2*n)

                    * Pentru simplificare, am evitat adaugarea numarului de operatii constante*

                In concluzie, algoritmul prezinta urmatoarele complexitati:

                    - Marginea superioara: T(n) este inclusa in O(n)
                    - Marginea inferioara: T(n) este inclusa in Ω(1)
                    - Complexitatea generala: O(n) este inclusa θ(n) 

        """
        #validate section
        search = persoana(0, nume, adresa)
        try:
            self.__valid.validator(search)
        except ValueError as e:
            raise ValueError(e)

        #search section
        lista = self.getAll()
        for pers in lista:
            if search.getNume() == None:
                if search.getAdresa() == pers.getAdresa():
                    return pers.getID()
            if search.getAdresa() == None:
                if search.getNume() == pers.getNume():
                    return pers.getID()
            if search.getNume() == pers.getNume() and search.getAdresa() == pers.getAdresa():
                    return pers.getID()
        

         
        



