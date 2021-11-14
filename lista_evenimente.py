from entity_repository import evenList_repo
from entities import eveniment
from validator import validEveniment

class listaEvenimente:
    def __init__(self):
        """Clasa pentru serviciul listei de evenimente
        """
        self.__index = 0
        self.__evenim = evenList_repo()
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

        self.__index += 1
        id = self.__index

        event = eveniment(id, data, timp, descriere)

        try:
            self.__validator.validator(event)
            self.__evenim.store(event)
        except ValueError as e:
            raise ValueError(e)

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
        
        if type(data) != None:
            even.setData(data)
        
        if type(timp) != None:
            even.setTimp(timp)
        
        if type(descriere) != None:
            even.setDescriere(descriere)

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



def test_addEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:16", "Antrenament sport")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament clarinet")
    
    assert(lst.getSize() == 3)

def test_stergeEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:16", "Antrenament fotbal")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament baschet")
    
    lst.stergeEveniment(1)
    lst.stergeEveniment(2)
    assert(lst.getSize() == 1)

    lst.addEveniment("22/12/2020", "10:16", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament programare")
    lst.stergeEveniment(3)
    assert(lst.getSize() == 2)
    
def test_modifEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Interviu companie random")
    lst.addEveniment("22/12/2020", "10:16", "Adunare voluntari")
    lst.addEveniment("22/12/2020", "10:17", "Strangere de fonduri")
    
    lst.modifEveniment(3, data=None, timp="11:12", descriere="Asculta-ma")
    assert(lst.getEveniment(lst.getEIndex(3)).getTimp() == "11:12")

def test_searchEvenim():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/11/2021", "13:12", "Antrenament baschet")
    lst.addEveniment("23/03/2019", "10:10", "Antrenament fotbal")

    ans = lst.searchEvenim(data = "22/12/2020")
    assert(len(ans) == 1 and ans[0] == 1)
    ans = lst.searchEvenim(timp = "13:12")
    assert(len(ans) == 1 and ans[0] == 2)
    ans = lst.searchEvenim(descriere = "Antrenament fotbal")
    assert(ans == 3)



test_addEveniment()
test_stergeEveniment()
test_modifEveniment()
test_searchEvenim()