import random
import obrazky
import sys

seznam = ["koření", "robča", "zlato"]
vybrane_slovo = random.choice(seznam)


def hrac (pole):
    pokusy = 0
    pismeno = input("Jaké tipuješ písmeno?: ")

    if pismeno in vybrane_slovo:
        return pole[:vybrane_slovo.index(pismeno)] + pismeno + pole[vybrane_slovo.index(pismeno) + 1:]

    else:
        pokusy += 1
        print("Toto písmeno tu není")
        return pole


def vyhodnoceni():
    pole = len(vybrane_slovo)*"_"
    print(pole)
    while True:
        if "_" in pole:
            pole = hrac(pole)
            print(pole)
        else:
         print ("Ty jsi ale holka šikovná! :-) ")
         break

#vyhodnoceni()
