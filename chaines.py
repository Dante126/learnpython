
def compte_car(chaine):
    compteur = 0
    for c in chaine:
        compteur+=1
    return compteur

def compte_voyelles(chaine):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    compteur = 0
    for c in chaine:
        if c in voyelles:
            compteur+=1
    return compteur

def compte_espaces(chaine):
    compteur = 0
    for c in chaine:
        if c == ' ':
            compteur += 1
    return compteur

def remplace_espaces(chaine, car):
    chaine2 = ""
    for c in chaine:
        if c == " ":
            chaine2 += car
        else:
            chaine2 += c
    return chaine2

chaine = "moi c'est Diallo, moi c'est Diallo"

print(compte_car(chaine))

print(compte_voyelles(chaine))

print(compte_espaces(chaine))

chaine2 = remplace_espaces(chaine, '-')
print(chaine2)


