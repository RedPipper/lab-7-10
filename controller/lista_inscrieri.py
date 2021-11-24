from repository import stocInscrieri

class listaInscrieri:
    def __init__(self):
        self.__legaturi = stocInscrieri()

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

def test_inscriePersoana():
    inscriere = listaInscrieri()
    inscriere.inscriePersoana(1,1)


    assert(len(inscriere.getInscrieri()) == 1 )

def test_inscrieriPers():
    inscriere = listaInscrieri()
    inscriere.inscriePersoana(1,1)
    inscriere.inscriePersoana(1,2)
    inscriere.inscriePersoana(1,3)

    rsp = inscriere.getInscrieriPers(1)
    
    assert(len(rsp) == 3)


test_inscrieriPers()
test_inscriePersoana()