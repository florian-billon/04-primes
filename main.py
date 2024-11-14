from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
    for d in range (2, int(sqrt(p)+1) ):
        if (p%d == 0):
            return False
    
    return True

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
