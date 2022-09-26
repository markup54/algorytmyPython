def szyfruj(slowo):
    klucz = "GADERYPOLUKI"
    zaszyfrowane=""
    for litera in slowo:
        if litera in klucz:
            ind =klucz.index(litera)
            if ind %2 == 0:
                litera = klucz[ind+1]
            else:
                litera = klucz[ind-1]

        zaszyfrowane = zaszyfrowane +litera
    return  zaszyfrowane

print("podaj słowo")
slowo=input().upper()
print(slowo)
zaszyfrowane_slowo = szyfruj(slowo)
print(zaszyfrowane_slowo)

