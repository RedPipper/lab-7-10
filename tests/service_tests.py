import unittest, os
from service.lista_evenimente import listaEvenimente
from service.lista_inscrieri import listaInscrieri
from service.lista_persoane import listaPersoane
class service_evenimente(unittest.TestCase):
    def setUp(self):
        self.lst = listaEvenimente("aux.txt")
        self.lst.addEveniment("22/12/2020", "10:15", "Antrenament colindat")
        self.lst.addEveniment("22/12/2020", "10:16", "Antrenament sport")
        self.lst.addEveniment("22/12/2020", "10:17", "Antrenament clarinet")

    def tearDown(self):
        os.remove("aux.txt")

    def test_addEvents(self):
        self.assertEqual(self.lst.getSize(), 3)

    def test_stergeEveniment(self):
        self.lst.stergeEveniment(3)
        self.assertEqual(self.lst.getSize(), 2)
        
        self.lst.stergeEveniment(2)
        self.assertEqual(self.lst.getSize(), 1)

    def test_modifEveniment(self):
        self.lst.modifEveniment(3, data=None,timp="11:12", descriere=None)
        self.assertEqual(self.lst.getEveniment(self.lst.getEIndex(3)).getTimp(), "11:12")

    def test_searchEvenim(self):

        ans = self.lst.searchEvenim(data = '22/12/2020')
        assert(len(ans) == 3 and ans[0] == 1)

        ans = self.lst.searchEvenim(timp = "10:16")
        assert(len(ans) == 1 and ans[0] == 2)

        ans = self.lst.searchEvenim(descriere = "Antrenament colindat")
        assert(ans == 1)

class service_persoane(unittest.TestCase):
    def setUp(self):
        self.lst = listaPersoane(0, "aux.txt")
        self.lst.addPersoana("Bolfa Alex", "Strada Pacii nr 23")
        self.lst.addPersoana("Iftode Vlad", "Pacurari")
        self.lst.addPersoana("Popescu Bianca", "Tatarasi")



    def tearDown(self):
        os.remove("aux.txt")

    def test_addEvents(self):
        self.assertEqual(self.lst.getSize(), 3)

    def test_stergeEveniment(self):
        self.lst.deletePersoana(3)
        self.assertEqual(self.lst.getSize(), 2)
        
        self.lst.deletePersoana(2)
        self.assertEqual(self.lst.getSize(), 1)

    def test_modifEveniment(self):
        self.lst.modifPers(1,nume="Nastasa Stefan", adresa=None)
        self.assertEqual(self.lst.getPersoana(self.lst.getPIndex(1)).getNume(), "Nastasa Stefan")

    def test_searchEvenim(self):

        ans = self.lst.searchPers(nume = "Popescu Bianca")
        assert(ans == 3)

        ans = self.lst.searchPers(nume = "Bolfa Alex")
        assert(ans == 1)

class service_inscrieri(unittest.TestCase):
    def setUp(self) -> None:
        self.lst = listaInscrieri("aux.txt")
        self.lst.inscriePersoana(1,1)
        self.lst.inscriePersoana(1,2)
        self.lst.inscriePersoana(1,3)

    def tearDown(self):
        os.remove("aux.txt")

    def test_inscriePers(self):
        assert(len(self.lst.getInscrieri()) == 3)

    def test_getInscrieriPers(self):
        assert(len(self.lst.getInscrieriPers(1)) == 3)





if __name__ == "__main__":
    unittest.main()
