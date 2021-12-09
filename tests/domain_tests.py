import domain.entities as en
import unittest

class person(unittest.TestCase):
    def setUp(self):
        self.pers = en.persoana(0,"Nastasa Stefan","adresa")
    
    def test_createPersoana(self):
        assert(self.pers.getID() == 0)
        assert(self.pers.getNume() == "Nastasa Stefan")
        assert(self.pers.getAdresa() == "adresa")
        
    def test_modifPersoana(self):
        self.pers.setNume("Stratan Alexia")
        self.pers.setAdresa("Pacurari.")
        self.pers.setId(2)

        assert(self.pers.getID() == 2)
        assert(self.pers.getAdresa() == "Pacurari.")
        assert(self.pers.getNume() == "Stratan Alexia")

class event(unittest.TestCase):
    def setUp(self):
        self.even = en.eveniment(0,"27/12/2021","18:00","asdfasdf")
    
    def test_createEveniment(self):
        assert(self.even.getID() == 0)
        assert(self.even.getData() == "27/12/2021")
        assert(self.even.getTimp() == "18:00")
        assert(self.even.getDescriere() == "asdfasdf")

        

        
    def test_modifPersoana(self):
        self.even.setTimp("12:34")
        self.even.setData("22/12/2021")
        self.even.setID(2)

        assert(self.even.getTimp() == "12:34")
        assert(self.even.getData() == "22/12/2021")
        assert(self.even.getID() == 2)

class legatura(unittest.TestCase):
    def setUp(self):
        self.legatura = en.legatura(1,1)

    def test_createLegatura(self):
        assert(self.legatura.getIDeven() == 1)
        assert(self.legatura.getIDpers() == 1)
    
    



if __name__ == "__main__":
    unittest.main()
