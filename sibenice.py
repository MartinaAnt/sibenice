import random

seznam = ("zajíc", "robča", "zlato")
vybrane_slovo = random.choice(seznam)
pole = len(vybrane_slovo)*"_"


pokusy = 0

pismeno = input("Jaké tipuješ písmeno?: ")
if pismeno in vybrane_slovo:
    return pole[:vybrane_slovo.index(pismeno)] + pismeno + pole[vybrane_slovo.index(pismeno) + 1:]
else:
    pokusy=pokusy+1
    print("Toto písmeno tu není")
    print(obrazek)
    print pole
