from entity_repository import evenList_repo
from entities import eveniment
class listaEvenimente:
    def __init__(self):
        """Clasa pentru serviciul listei de evenimente
        """
        self.__index = 0
        self.__evenim = evenList_repo()

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
            event.validate()
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
            aux_even.validate()
        except ValueError as e:
            raise e
        
        if type(data) != None:
            even.setData(data)
        
        if type(timp) != None:
            even.setTimp(timp)
        
        if type(descriere) != None:
            even.setDescriere(descriere)


def test_addEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:16", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament colindat")
    
    assert(lst.getSize() == 3)

def test_stergeEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:16", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament colindat")
    
    lst.stergeEveniment(1)
    lst.stergeEveniment(2)
    assert(lst.getSize() == 1)

    lst.addEveniment("22/12/2020", "10:16", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament colindat")
    lst.stergeEveniment(3)
    assert(lst.getSize() == 2)
    
def test_modifEveniment():
    lst = listaEvenimente()
    lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:16", "Antrenament colindat")
    lst.addEveniment("22/12/2020", "10:17", "Antrenament colindat")
    
    lst.modifElem(3, data=None, timp="11:12", descriere="Asculta-ma")
    assert(lst.getEveniment(lst.getEIndex(3)).getTimp() == "11:12")

test_addEveniment()
test_stergeEveniment()