import random

# Tirer un nombre entre 0 et 100
nombre = random.randint(0,100)

trouve = False
essais = 0

while not trouve:
    # Demander un nombre à l'utilisateur
    essais += 1
    n = input("Entrez un nombre entre 0 et 100: ")
    n = (int)(n)

    # Tester si le nombre est le bon
    if n == nombre:
        trouve = True
        print("C'est gagné en %d essais" % essais)
    # Tester s'il est plus grand ou plus petit
    elif n < nombre:
        print("Trop petit")
    else:
        print("Trop grand")
