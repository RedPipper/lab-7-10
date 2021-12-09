import unittest, os
from repository.evenList_frepo import evenlist_frepo
from repository.persList_frepo import perslist_frepo
from repository.legatura_frepo import stocInscrieri

from domain.entities import eveniment, persoana, legatura

class evenList_repo(unittest.TestCase):
    def setUp(self):
        self.aux = evenlist_frepo(filename="aux.txt")
        self.aux.store(eveniment(1,"10/12/2021","10:12","descriere 1"))
        self.aux.store(eveniment(2,"10/12/2021","10:12","descriere 2"))
        
    def tearDown(self):
        os.remove("aux.txt")

    def test_read_write(self):
        rasp = self.aux.getAll()
        self.assertEqual(len(rasp), 2)
        self.assertEqual(rasp[0], eveniment(1,"10/12/2021","10:12","descriere 1"))

    def test_size(self):
        self.assertEqual(self.aux.size(), 2)

    def test_deleteElem(self):
        self.aux.deleteElem(1)
        self.assertEqual(self.aux.size(), 1)
        self.assertRaises(ValueError, lambda:self.aux.deleteElem(1))

    def test_getElem(self):
        e = self.aux.getElem(0)
        self.assertEqual(e, eveniment(1,"10/12/2021","10:12","descriere 1"))
        self.assertRaises(ValueError, lambda:self.aux.getElem(12))
            
class persList_repo(unittest.TestCase):
    def setUp(self):
        self.aux = perslist_frepo(filename="aux.txt")
        self.aux.store(persoana(0,"Nastasa Stefan","adresa"))
        self.aux.store(persoana(1,"Nastasa Stefan","adresa"))
        
    def tearDown(self):
        os.remove("aux.txt")

    def test_read_write(self):
        rasp = self.aux.getAll()
        self.assertEqual(len(rasp), 2)
        self.assertEqual(rasp[0], persoana(0,"Nastasa Stefan","adresa"))

    def test_size(self):
        self.assertEqual(self.aux.size(), 2)

    def test_deleteElem(self):
        self.aux.deleteElem(1)
        self.assertEqual(self.aux.size(), 1)
        self.assertRaises(ValueError, lambda:self.aux.deleteElem(1))

    def test_getElem(self):
        e = self.aux.getElem(0)
        self.assertEqual(e, persoana(0,"Nastasa Stefan","adresa"))
        self.assertRaises(ValueError, lambda:self.aux.getElem(12))

class inscList_repo(unittest.TestCase):
    def setUp(self):
        self.aux = stocInscrieri(filename="aux.txt")
        self.aux.storeInscriere(1,1)
        self.aux.storeInscriere(1,2)
        
    def tearDown(self):
        os.remove("aux.txt")

    def test_read_write(self):
        rasp = self.aux.getAll()
        self.assertEqual(len(rasp), 2)
        self.assertEqual(rasp[0], legatura(1,1))

    





if __name__ == "__main__":
    unittest.main()

        
