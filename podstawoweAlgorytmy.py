#algorytmy tekstowe
#palindrom
#wczytaj słowo i sprawdź czy jest palindromem

def czyPalindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    return False

print("podaj słowo")
slowo=input()
if czyPalindrom(slowo):
    print(slowo, "jest palindromem")
else:
    print(slowo,"nie jest palindromem")

# anagramy
#sprawdź czy dwa słowa są anagramami czyli składają się z takich samych liter w tej samej liczbie

def czyAnagramy(slowo1,slowo2):
    lista1=list(slowo1)
    lista2 = list(slowo2)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    return False

slowo1=input()
slowo2=input()
if czyAnagramy(slowo1,slowo2):
    print("tak")
else:
    print("nie")

#wczytaj slowo i powiedz jaka litera występuje najwięcej razy i ile
slowo = "ejjżyraafaryżje"

zbiorLiter = set(slowo)
maks = 0
teLitery =[]
for litera in zbiorLiter:
    if maks<slowo.count(litera):
        maks = slowo.count(litera)
        taLitera = litera
        teLitery = [litera]
    elif maks == slowo.count(litera):
        teLitery.append(litera)

print(teLitery,maks)

#wczytaj liczbę i sprawdź czy jest liczbą pierwszą
print("podaj liczbę")
liczba=int(input())
def czyPierwsza (liczba):
    for i in range(2,int(liczba**0.5+1)+1):
        if liczba % i == 0:
            return False
    return True

if czyPierwsza(liczba):
    print(liczba,"jest pierwsza")

#wypisz wszystkie liczby pierwsze mniejsze od liczby wczytanej
pierwsze1 =[1 for i in range(liczba+1)]
pierwsze2 = []
for i in range(liczba+1):
    pierwsze2.append(1)
pierwsze1[0]=0
pierwsze1[1]=0
for i in range(2,liczba+1): #zlozoność na pierwiastek
    if pierwsze1[i] == 1:
        for k in range(2*i,liczba+1,i):
            pierwsze1[k]=0


for i in range(liczba+1):
    if pierwsze1[i] == 1:
        print(i)

print("podaj dwie liczby")

a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print(a)