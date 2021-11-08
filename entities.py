""" 
Modul care contine entitatile programului (persoana si eveniment)
"""

class persoana:
    def __init__(self, IDp, nume, adresa):
        """Clasa pentru gestionarea informatiile unei persoane

        Args:
            IDp (int): ID-ul persoanei
            nume (string): Numele persoanei
            adresa (string): Adresa persoanei
        """
        self.__personID = IDp
        self.__nume = nume
        self.__adresa = adresa

    def getID(self):
        return self.__personID
    
    def getNume(self):
        return self.__nume

    def getAdresa(self):
        return self.__adresa

    def setId(self, IDp):
        self.__personID = IDp
    
    def setNume(self, nume):
        self.__nume = nume

    def setAdresa(self, adresa):
        self.__adresa = adresa
        
    def __eq__(self, other):
        """Defineste conceptul de egalitate intre persoane
        pers1 == pers2

        return True daca pers self este egala cu pers other
        """
        if self.__nume == other.getNume() and self.__adresa == other.getAdresa():
            return True
        
        return False

    def __str__(self):
        """Afiseaza informatiile persoanei intr-un format predefinit

        Returns:
            [type]: [description]
        """
        return "Persoana cu ID-ul: "+ str(self.__personID) + "\n" + "       Numele: " + self.__nume + '\n' + "     Adresa: " + self.__adresa + '\n' 
    
def test_createPersoana():
    pers1 = persoana(1, "Robert Codreanu", "Undeva la tara")
    assert(pers1.getID() == 1)
    assert(pers1.getNume() == "Robert Codreanu")
    assert(pers1.getAdresa() == "Undeva la tara")

    pers1.setNume("Stratan Alexia")
    pers1.setAdresa("Pacurari.")
    pers1.setId(2)

    assert(pers1.getID() == 2)
    assert(pers1.getAdresa() == "Pacurari.")
    assert(pers1.getNume() == "Stratan Alexia")

test_createPersoana()


class eveniment:
    def __init__(self, IDe, data, timp, descriere):
        """Clasa creata pentru gestionarea unui singur eveniment

        Args:
            IDe (int): Id-ul evenimentului
            data (string): Data in format zz/ll/aaaa
            timp (string): Timpul in format hh:mm (24 ore)
            descriere (string): Descriere evenimentului
        """
        self.__ID = IDe
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def getID(self):
        return self.__ID

    def getData(self):
        return self.__data

    def getTimp(self):
        return self.__timp
    
    def getDescriere(self):
        return self.__descriere

    def setID(self, IDe):
        self.__ID = IDe
    
    def setData(self, data):
        self.__data = data

    def setTimp(self, timp):
        self.__timp = timp
    
    def setDescriere(self, descriere):
        self.__descriere = descriere

    def validate(self):
        """Valideaza datele din obiect
        """

        

    def __str__(self) -> str:
        """Afiseaza datele evenimentului intr-un format predefinit

        Returns:
            str
        """
        return "Evenimentul cu ID-ul: " + str(self.__ID) + '\n' + "        Data: " + self.__data + '\n' + "        Timp: " + self.__timp + '\n' + "        Descriere: " + self.__descriere + '\n'
        




def test_creatEveniment():
    even = eveniment(1, "12/02/2022", "12:02", "Eveniment random")
    assert(even.getID() == 1)
    assert(even.getDescriere() == "Eveniment random")
    assert(even.getData() == "12/02/2022")
    assert(even.getTimp() == "12:02")
    
    even.setTimp("12:34")
    even.setData("22/12/2021")
    even.setID(2)

    assert(even.getTimp() == "12:34")
    assert(even.getData() == "22/12/2021")
    assert(even.getID() == 2)
    

test_creatEveniment()

    