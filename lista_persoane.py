"""
Modul care contine listele de entitati si operatiile 
care pot fi realizate pe acestea
"""
from entity_repository import persList_repo
from entities import persoana
from validator import validPersoana
class listaPersoane:
    def __init__(self, index = 0):
        """
        Serviciul pentru administrare a listei de persoane
            
            index (int): punctul de indexare al id-urilor listei
        """
        self.__index = index*1000
        self.__persoane = persList_repo()
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
        self.__index += 1
        id = self.__index

        pers = persoana(id, nume, adresa)

        try: 
            self.__valid.validator(pers)
            self.__persoane.store(pers)
        
        except ValueError as e:
            raise ValueError(e)

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
        
        return None
    
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

    def searchPers(self, nume=None, adresa=None):
        """Cauta persoane dupa nume, adresa sau ambele.

        Args:
            nume (str, optional): Numele persoanei cautate. Defaults to None.
            adresa (str, optional): Adresa persoanei cautate. Defaults to None.

        Raises:
            ValueError: Datele introduse sunt gresite

        Returns:
            int: index-ul persoanei
        """
        #validate section
        search = persoana(0, nume, adresa)
        try:
            self.__valid.validator(search)
        except ValueError as e:
            raise ValueError(e)

        #search section
        lista = self.getAll()
        for index, pers in enumerate(lista):
            if search.getNume() == None:
                if search.getAdresa() == pers.getAdresa():
                    return pers.getID()
            if search.getAdresa() == None:
                if search.getNume() == pers.getNume():
                    return pers.getID()
            if search.getNume() == pers.getNume() and search.getAdresa() == pers.getAdresa():
                return pers.getID()
        

         
        
def test_addPerson():
    perslist = listaPersoane(0)

    perslist.addPersoana("Bolfa Alex", "Strada Pacii nr 23")
    assert(perslist.getSize() == 1)
    
    perslist.addPersoana("Iftode Vlad", "Pacurari.")
    assert(perslist.getSize() == 2)

def test_deletePerson():
    perslist = listaPersoane(0)
    perslist.addPersoana("Bolfa Alex", "Strada Pacii nr 23")
    perslist.deletePersoana(1)
    assert(perslist.getSize() == 0)

def test_modifPerson():
    perslist = listaPersoane(0)
    perslist.addPersoana("Bolfa Alex", "Strada Pacii nr 23")
    perslist.addPersoana("Iftode Vlad", "Strada Pacii nr 18")
    perslist.modifPers(1, "Iftode George", None)

    index = perslist.getPIndex(1)
    pers = perslist.getPersoana(index)
    assert(pers.getNume() == "Iftode George")
    
def test_searchPersoana():
    perslist = listaPersoane(0)
    perslist.addPersoana("Bolfa Alex", "Strada Pacii nr 23")
    perslist.addPersoana("Iftode Vlad", "Strada Pacii nr 18")
    perslist.addPersoana("Bulacovschi Ana", "Strada nr 15")
    perslist.addPersoana("Stratan Alexia", "Strada Pacii nr 17")


    
    ans = perslist.searchPers(nume = "Stratan Alexia")
    assert(ans == 4)
    ans = perslist.searchPers(nume = "Bolfa Alex")
    assert(ans == 1)
    ans = perslist.searchPers(adresa="Strada Pacii nr 17")
    assert(ans == 4)



    


    

test_deletePerson()
test_addPerson()
test_modifPerson()
test_searchPersoana()


