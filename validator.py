from entities import persoana, eveniment

class validPersoana:

    
    def validator(self, pers:persoana):
        """Valideaza informatiile din obiect
        """
        if type(pers.getID()) != int:
            raise ValueError("Wrong id type")
        
        if type(pers.getNume()) != str and type(pers.getNume()) != None :
            raise ValueError("Wrong name type")
        else:
            if len(pers.getNume().split(" "))<2:
                raise ValueError("Numele trebuie sa contina cel putin doua cuvinte")


class validEveniment:

    def validator(self, event:eveniment):
        if type(event.getID()) != int :
            raise ValueError("Wrong id type")
        
        if type(event.getData()) != str and type(event.getData()) != None:
            raise ValueError("Wrong data type")
        else:
            if event.getData().find("/"):
                if len(event.getData().split("/")) != 3:
                    raise ValueError("Wrong data format")
            else:
                raise ValueError("Wrong data format")
        
        if type(event.getTimp() ) != str and type(event.getTimp()) != None:
            raise ValueError("Wrong timp type")
        else:
            if event.getTimp().find(":"):
                a = event.getTimp().split(":")
                if len(event.getTimp().split(":")) != 2:
                    raise ValueError("Wrong timp format")
            else:
                raise ValueError("Wrong timp format")

        if type(event.getDescriere()) != str and type(event.getDescriere()) != None :
            raise ValueError("Wrong descriere type")
