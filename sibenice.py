import random
import obrazky

seznam_slov = ["koření", "robča", "zlato"]
vybrane_slovo = random.choice(seznam_slov)
seznam_pokusu = []
pouzita = []

def hrac (pole):
    pismeno = input("Jaké tipuješ písmeno?: ")
    if pismeno.isdigit() or pismeno not in vybrane_slovo or (pismeno in vybrane_slovo and len(pismeno)!=1):
        if pismeno.isdigit():
            print("Číslo....vážně?!?")
        elif pismeno == "" or pismeno.isspace():
            print("Fujko, to bylo co?")
        elif len(pismeno)!=1:
            print("Pomalu, zadáváme pouze po jednom písmenu ;-)")
        elif pismeno in pouzita:
            print("Fakt tam není")
        else:
            pouzita.append(pismeno)
            print("Toto písmeno tu není")
        seznam_pokusu.append(len(seznam_pokusu))
        obrazky.seznam[seznam_pokusu[-1]]()
        return pole
    else:
        print("Paráda, trefila ses!")
        return pole[:vybrane_slovo.index(pismeno)] + pismeno + pole[vybrane_slovo.index(pismeno) + 1:]

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
