from domain.entities import legatura
import os

class stocInscrieri:
    def __init__(self, filename="data/legaturi.txt"):
        self.__file = filename

    def __write_all_to_file(self, legaturi:list):
        """writes all persons from pers to the file

        Args:
            pers (list): list of persons to be written
        """
        with open(self.__file, 'w') as f: 
            for leg in legaturi:
                f.write(leg.storeFormat() + '\n')
            
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
                l = list(int(a) for a in l)
                response.append(legatura(*l))
        
            f.close()
        
        except IOError as e:
            print(e)
            self.__write_all_to_file([])
        
        return response
    
    def storeInscriere(self, IDevent, IDpersoana):
            inscriere = legatura(IDpersoana, IDevent)
            
            legList = self.__load_all_from_file()
            legList.append(inscriere)
            self.__write_all_to_file(legList)
        
    def getAll(self):
        return self.__load_all_from_file()


def test_store_read():
    aux = stocInscrieri(filename="aux.txt")
    aux.storeInscriere(1,1)
    aux.storeInscriere(1,2)

    resp = aux.getAll()
    os.remove("aux.txt")
    assert(len(resp) == 2)

test_store_read()

