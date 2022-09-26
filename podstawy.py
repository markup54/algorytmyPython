zmienna = 12
print("podaj liczbę")
liczba=int(input())
print(liczba)
if liczba%2 == 0:
    print(liczba,"jest parzysta")
else:
    print(liczba," jest nieparzysta ")

#wypisz liczby dwucyfrowe parzyste
for i in range(10,100,2):
    print(i,end=", ")

slowo="informatyka"
print(slowo)
for litera in slowo:
    print(litera, ord(litera) )

while liczba!=0:
    print("podaj 0")
    liczba=int(input())

import random
losowe = [];
for i in range(10):
    wylosowana = random.randint(1,10);
    losowe.append(wylosowana)
print(losowe)
losowe.sort()
print(losowe)
print(sum(losowe))
print(min(losowe))
print(max(losowe))

zbior = set(losowe)
#wypisz ile razy wylosowały się poszczególne liczby
for element in zbior:
    print(element,losowe.count(element))