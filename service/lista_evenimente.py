from repository.evenList_frepo import evenlist_frepo
from domain.entities import eveniment
from validator.validator import validEveniment
import os

class listaEvenimente:
    def __init__(self, filename = 'data/evenlist.txt'):
        """Clasa pentru serviciul listei de evenimente
        """
        self.__index = 0
        self.__evenim = evenlist_frepo(filename)
        self.__validator = validEveniment()

    def getAll(self):
        return self.__evenim.getAll()

    def getSize(self):
        return self.__evenim.size()

    def addEveniment(self, data, timp, descriere):
        """Adauga un eveniment in lista

        Args:
            data (str): data evenimentului
            timp (str): timpul evenimentului
            descriere (str): descrierea evenimentului

        Raises:
            ValueError: formatul datelor gresit/ error handling
        """

        id = self.__evenim.size() + 1

        event = eveniment(id, data, timp, descriere)

        try:
            self.__validator.validator(event)
        except ValueError as e:
            raise ValueError(e)

        evnts = self.__evenim.getAll()
        for e in evnts:

            if e == event:
                raise ValueError("Evenimentul există deja în listă.")
        
        self.__evenim.store(event)


    def getEIndex(self, id):
        """Returneaza index-ul evenimentului cu id-ul dat

        Args:
            id (int): id-ul unui eveniment

        Returns:
            int: index-ul din lista al evenimentului
        """

        lst = self.__evenim.getAll()
        for i,even in enumerate(lst):
            if even.getID() == id:
                return i

    def stergeEveniment(self, id):
        """Sterge eveniment

        Args:
            id (int): id-ul evenimentului de sters
        """
        index = self.getEIndex(id)
        self.__evenim.deleteElem(index)

    def getEveniment(self, index):
        """Returneaza un obiect eveniment corespunzator

        Args:
            index (int): index-ul la care se gaseste obiectul

        Returns:
            eveniment
        """
        return self.__evenim.getElem(index)

    def modifEveniment(self, id, data=None, timp=None, descriere=None):
        """Modifica evenimentul cu id-ul dat

        Args:
            id (int): id-ul unui eveniment
            data (str, optional): Data modificata. Defaults to None.
            timp (str, optional): Timpul modificat. Defaults to None.
            descriere (str, optional): Descrierea modificata. Defaults to None.

        Raises:
            e: error handling
        """
        pos = self.getEIndex(id)
        even = self.getEveniment(pos)

        aux_even = eveniment(0, data, timp, descriere)

        try:
            self.__validator.validator(aux_even)
        except ValueError as e:
            raise e
        
        if data != None:
            even.setData(data)
        
        if timp != None:
            even.setTimp(timp)
        
        if descriere != None:
            even.setDescriere(descriere)
        
        allE = self.getAll()
        allE[pos] = even
        self.__evenim.modifLista(allE)

    def searchEvenim(self, data=None, timp=None, descriere=None):
        """Cauta si returneaza evenimentele cu aceeasi data sau timp si returneaza un singur eveniment 
        cu aceeasi descriere (se presupune ca evenimentele au descrieri diferite).

        Args:
            data (str, optional): Data evenimentului cautat. Defaults to None.
            timp (str, optional): Ora/Timpul evenimentului cautat. Defaults to None.
            descriere (str, optional): Descrierea evenimentului cautat. Defaults to None.

        Raises:
            e: O data introdusa incorect

        Returns:
            lst: lista cu evenimentele cautate
            int: indexul evenimentului cu descrierea cautata
        """
        aux_even = eveniment(0, data, timp, descriere)

        try:
            self.__validator.validator(aux_even)
        except ValueError as e:
            raise e
        
        lst = self.getAll()
        rsp = []
        for index, evenim in enumerate(lst):
            if evenim.getData() == data or evenim.getTimp() == timp:
                rsp.append(evenim.getID())
            
            if evenim.getDescriere() == descriere:
                return evenim.getID()

        return rsp 
