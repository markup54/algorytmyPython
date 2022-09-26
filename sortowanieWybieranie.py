def wczytajTablice():
    listaWczytanych = []
    print("podaj 10 liczb")
    for i in range(10):
        print("podaj element", i)
        listaWczytanych.append(int(input()))
    return listaWczytanych


def szukajMaks(lista, indeks):
    maksymalna = lista[indeks]
    zwroconyIndeks = indeks
    for i in range(indeks + 1, len(lista)):
        if maksymalna < lista[i]:
            maksymalna = lista[i]
            zwroconyIndeks = i
    return zwroconyIndeks


def sortuj(lista):
    """
    funkcja sortuje tablicę przez wybieranie
    :argument lista: tablica do posortowania
    :return: posortowaną tablicę
    """
    for i in range(len(lista) - 1):
        indeks = szukajMaks(lista, i)
        lista[i], lista[indeks] = lista[indeks], lista[i]

    return lista


tablica = wczytajTablice()
print(tablica)
print(szukajMaks(tablica, 3))
print("posortowane malejąco")
print(sortuj(tablica))
#print(print.__doc__)
print(sortuj.__doc__)