import random 
import string
from datetime import date
from time import sleep

def genPersoana():
    """Generează un nume și o adresă a unei persoane.
    """
    nume = ""
    for i in range(2):
        nume += ''.join(random.choice(string.ascii_uppercase)) 
        nLen = random.randint(3,7)
        nume +=  ''.join(random.choice(string.ascii_lowercase) for i in range(nLen) ) 
        nume+=' '
    
    nume = nume[:-1]
    adresa = ""
    aLen = random.randint(2,6)

    for i in range(aLen):
        adresa+=''.join(random.choice(string.ascii_uppercase))
        nLen = random.randint(3,8)
        adresa+= ''.join(random.choice(string.ascii_lowercase) for _ in range(nLen))
        adresa+= " "

    adresa = adresa[:-1]
    return (nume, adresa)

def genEvent():
    """Generează un eveniment viitor"""
    data = ""
    timp = ""
    descriere = ""

    dLen = random.randint(10, 50)
    for i in range(dLen):
        if i==0:
            descriere += ''.join(random.choice(string.ascii_uppercase))

        cuvLen = random.randint(2, 13)
        descriere += ''.join(random.choice(string.ascii_lowercase) for _ in range(cuvLen))
        descriere += " "

    ora = random.randint(0,23)
    minute = random.randint(1,59)
    
    timp = ''.join('0'+str(ora) if ora < 10 else str(ora))
    timp += ":"
    timp += ''.join('0' + str(minute) if minute <10 else str(minute))

    an = random.randint(date.today().year, 2050)
    luna = random.randint(date.today().month,12) if an == date.today().year else random.randint(1,12)
    ziua = random.randint(1,31) if luna in [1,3,5,7,8,10,12] else random.randint(1,30)
    
    if luna == 2 and ziua >=28:
        if an % 4 == 0:
            ziua = 29
        else:
            ziua = 28

    data = str(ziua) if ziua>=10 else '0'+str(ziua)
    data += '/' + str(luna) if luna>=10 else '/' + '0'+str(luna)  
    data+='/' + str(an)


    descriere = descriere[:-1]
    return (data, timp, descriere)


if __name__ == "__main__":
    while True:
        print(genPersoana())
        print(genEvent())
        print()
        sleep(2)
    

