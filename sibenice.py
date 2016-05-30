import random
import obrazky

seznam_slov = ["koření", "robča", "zlato"]
vybrane_slovo = random.choice(seznam_slov)
seznam_pokusu = []
pouzita = []

def hrac (pole):
    pismeno = input("Jaké tipuješ písmeno?: ")
    if pismeno in vybrane_slovo:
        return pole[:vybrane_slovo.index(pismeno)] + pismeno + pole[vybrane_slovo.index(pismeno) + 1:]
    else:
        if pismeno in pouzita:
            print("Fakt tam není")
        else:
            print("Toto písmeno tu není")
        seznam_pokusu.append(len(seznam_pokusu))
        obrazky.seznam[seznam_pokusu[-1]]()
        pouzita.append(pismeno)
        return pole

def hra():
    pole = len(vybrane_slovo)*"_"
    print(pole)
    while True:
        if len(seznam_pokusu) > 8:
            print("Game Over")
            break
        elif "_" in pole:
            pole = hrac(pole)
            print(pole)
        else:
            print ("Ty jsi ale holka šikovná! :-) ")
            break

hra()
