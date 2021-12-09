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
    
    def storeFormat(self):
        return "{}||{}||{}".format(self.__personID, self.__nume, self.__adresa)

    def __eq__(self, other):
        """Defineste conceptul de egalitate intre persoane
        pers1 == pers2

        return True daca pers self este egala cu pers other
        """
        if ( self.__nume == other.getNume() and self.__adresa == other.getAdresa()):
            return True

        

        return False

    def __str__(self):
        """Afiseaza informatiile persoanei intr-un format predefinit

        Returns:
            [type]: [description]
        """
        return "Persoana cu ID-ul: "+ str(self.__personID) + "\n" + "       Numele: " + self.__nume + '\n' + "     Adresa: " + self.__adresa + '\n' 

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

    def storeFormat(self):
        return "{}||{}||{}||{}".format(self.__ID, self.__data, self.__timp, self.__descriere)

    def __eq__(self, other):
        if self.__descriere.replace(" ","") == other.getDescriere().replace(" ",""):
            return True
        
        return False

    def __str__(self) -> str:
        """Afiseaza datele evenimentului intr-un format predefinit

        Returns:
            str
        """
        return "Evenimentul cu ID-ul: " + str(self.__ID) + '\n' + "        Data: " + self.__data + '\n' + "        Timp: " + self.__timp + '\n' + "        Descriere: " + self.__descriere + '\n'
        


class legatura:
    def __init__(self, IDp, IDe):
        self.__IDp = IDp
        self.__IDe = IDe

    def getIDpers(self):
        return self.__IDp

    def getIDeven(self):
        return self.__IDe

    def storeFormat(self):
        return "{}||{}".format(self.__IDp, self.__IDe)

    def __eq__(self, __o: object):
        return self.__IDp == __o.getIDpers() and self.__IDe == __o.getIDeven()

