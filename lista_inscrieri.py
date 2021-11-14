from entity_repository import stocInscrieri

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

def test_inscriePersoana():
    inscriere = listaInscrieri()
    inscriere.inscriePersoana(1,1)


    assert(len(inscriere.getInscrieri()) == 1 )

test_inscriePersoana()