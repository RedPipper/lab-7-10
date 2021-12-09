from domain.entities import eveniment
import os

class evenlist_frepo:

    def __init__(self, filename = 'data/evenlist.txt'):
        self.__file = filename
    
    def __write_all_to_file(self, events:list):
        """writes all persons from pers to the file

        Args:
            pers (list): list of persons to be written
        """
        with open(self.__file, 'w') as f: 
            for e in events:
                f.write(e.storeFormat() + '\n')
            
        f.close()

    def __load_all_from_file(self):
        """Reads all persons from file

        Raises:
            e: IOexception

        Returns:
            list : list of persons from file
        """
        response = []
        try:
            f = open(self.__file, 'r')
            lines = f.readlines()
            for l in lines:
                l = l[:-1]
                l = l.split("||")
                l[0] = int(l[0])
                response.append(eveniment(*l))
        
            f.close()
        
        except IOError as e:
            print(e)
            self.__write_all_to_file([])
            


        return response

    def getAll(self):
        """Returneaza toate persoanele din fisier
        """
        return self.__load_all_from_file()

    def store(self, e:eveniment):
        """Adauga o persoana in fisier

        Args:
            p (persoana): persoana care trebuie adaugata
        """
        pList = self.__load_all_from_file()
        pList.append(e)

        self.__write_all_to_file(pList)
    
    def size(self):
        """Returns the number of persons from the file

        Returns:
            int: size of the list/nr of persons
        """
        pList = self.__load_all_from_file()
        return len(pList)

    def deleteElem(self, pos:int):
        if pos < self.size():
            pList = self.__load_all_from_file()
            pList.pop(pos)
            self.__write_all_to_file(pList)
        else:
            raise ValueError("Nu exista.")
        
    def getElem(self, pos):
        if pos < self.size():
            pList = self.__load_all_from_file()
            return pList[pos]
        else:
            raise ValueError("Nu exista.")


def test_read_write():
    aux = evenlist_frepo(filename="aux.txt")
    aux.store(eveniment(1,"10/12/2021","10:12","descriere ma"))
    aux.store(eveniment(1,"10/12/2021","10:12","descriere ma"))
    
    resp = aux.getAll()
    os.remove("aux.txt")
    assert(len(resp) == 2)

test_read_write()


