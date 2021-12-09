from repository.legatura_frepo import stocInscrieri
import os
import math 
import itertools

class listaInscrieri:
    def __init__(self, filename = "data/inscrieri.txt"):
        self.__legaturi = stocInscrieri(filename)

    def inscriePersoana(self, IDp, IDe):
        inscrieri = self.__legaturi.getAll()
        
        for insc in inscrieri:
            if insc.getIDeven() == IDe and insc.getIDpers() == IDp:
                raise ValueError("Persoana este înscrisă deja la acest eveniment.")
        
        self.__legaturi.storeInscriere(IDe, IDp)

    def getInscrieri(self):
        return self.__legaturi.getAll()

    def getInscrieriPers(self, IDp):
        """Returneaza id-ul evenimentelor la care este inscrisa o persoana

        Args:
            IDp (int): [description]
        """
        insc = self.getInscrieri()
        rsp = []
        for inst in insc:
            if inst.getIDpers() == IDp:
                rsp.append(inst.getIDeven())

        return rsp

    def topPersoane(self):
        inscrieri = self.getInscrieri()
        rasp = {}
        for insc in inscrieri:
            if insc.getIDpers() not in rasp.keys():
                rasp[insc.getIDpers()] = 1
            else:
                rasp[insc.getIDpers()] += 1
        
        pList = []
        maxi = 0
        for pers in rasp.keys():
            if rasp[pers] > maxi:
                pList.clear()
                maxi = rasp[pers]
                pList.append(pers)
            elif rasp[pers] == maxi:
                pList.append(pers)
        
        return pList

    def topEvenim(self):
        percentage = 20/100
        inscrieri = self.getInscrieri()
        rasp = {}
        for insc in inscrieri:
            if insc.getIDeven() not in rasp.keys():
                rasp[insc.getIDeven()] = 1
            else:
                rasp[insc.getIDeven()] += 1
        
        rasp = dict(sorted(rasp.items(), key= lambda item: item[1], reverse=True))
        l = len(rasp)
        rasp = dict(itertools.islice(rasp.items(), math.floor(percentage * l)))
        return rasp

def test_inscriePersoana():
    inscriere = listaInscrieri("aux.txt")
    inscriere.inscriePersoana(1,1)

    try:
        assert(len(inscriere.getInscrieri()) == 1 )
    except AssertionError as e:
        os.remove("aux.txt")
        raise e
    os.remove("aux.txt")
    

def test_inscrieriPers():
    inscriere = listaInscrieri("aux.txt")
    inscriere.inscriePersoana(1,1)
    inscriere.inscriePersoana(1,2)
    inscriere.inscriePersoana(1,3)

    rsp = inscriere.getInscrieriPers(1)
    try:
        assert(len(rsp) == 3)
    except AssertionError as e:
        os.remove("aux.txt")
        raise e
    
    os.remove("aux.txt")



test_inscrieriPers()
test_inscriePersoana()