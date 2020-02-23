import sys


def minimum(liste):
    min = sys.maxsize
    for i in liste:
        if i < min:
            min = i
    return min


def maximum(liste):
    max = -sys.maxsize
    for i in liste:
        if i > max:
            max = i
    return max


def minmax(liste):
    min = minimum(liste)
    max = maximum(liste)
    return min, max


def moyenne(liste):
    resultat = 0
    for i in liste:
        resultat += i
    resultat /= len(liste)
    return resultat


def pair_zero(liste):
    liste2 = []
    for i in liste:
        if i % 2 == 0:
            liste2.append(0)
        else:
            liste2.append(i)
    return liste2


def inverse(liste):
    liste2 = []
    for i in liste:
        liste2.insert(0, i)
    return liste2


def inverse2(liste):
    liste2 = []
    for i in range(-1, -len(liste) - 1, -1):
        liste2.append(liste[i])
    return liste2


l = [5, 7, 2, -3, 8, -6, 0, 12, 1]

min = minimum(l)
print(min)

max = maximum(l)
print(max)

min, max = minmax(l)
print(min, max)

moy = moyenne(l)
print(moy)

l2 = pair_zero(l)
print(l2)

l2 = inverse(l)
print(l2)

l2 = inverse2(l)
print(l2)
