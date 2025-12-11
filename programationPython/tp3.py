# Bonjour MR IMAM , je suis Bayad Zakaria , j'ai choisie de renomer les exercices en partie 1 2 .... pour une meilleur claritée

import utils

# PARTIE1
# EX1


def somme(a, b):
    return a + b


# EX2


def afficher_message(msg):
    print(msg)


# EX3


def operations(a, b):
    return a + b, a * b


a, b = operations(1, 1)

# EX4

n1 = int(input("Donnner le 1er chiffre\n"))
n2 = int(input("Donnner le 2er chiffre\n"))
msg = input("Donner votre nom\n")

print(somme(n1, n2))
print(a, b)

afficher_message("Bonjour " + msg + " . Bienvenue a NEOVIM")

# PARTIE2

# 1- resultat sera 15
# 2- X sera 10
# 3- X est une variable global , la 2eme déclaration de X est sur ajouter_cinq() resultat prend alors ce le return de la function

# PARTIE3
# EX1 : check Utils

# EX2

N = int(input("Donner une nombre"))

print(utils.carre(N))
print(utils.est_pair(N))
utils.fin_traitement()


# EX3

# De un c'est pour une meilleur lisibilité , de deux la compilation du code prendra bcp de temps , enfin da dépend mais avoir un module est import seulement ce qu'il faut est bien mieu profetionel , en plus si on a une fonction qu'on utilise plusieur fois c'est mieu de la déclarer dans un fichier /lib , c'est les bases du principe SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion)

# PARTIE4

# EX1

L = [3, 8, 2, 9, 5]

for idx, i in enumerate(L):
    print(idx, i)

L.append(12)

L.pop(1)

print(L)

# EX2

date = (2025, 3, 15)

print(date[0])

# Un tuple comparer a une list n'est pas modifiable , c'est une caracteristique de l'object sur python ,d'ailleur je ne pense pas que les tuples exist sur C ou JAVA , c'est (a ma connaisance) le seul language qui a ce genre d'object


# EX3

etu = {"nom": "Sara", "age": 21, "ville": "Rabat"}

print(etu["nom"], etu["age"])

etu["note"] = 15.5

etu["ville"] = "Casablanca"

# EX4

E = {3, 6, 6, 9, 12}

print(E)

E.add(15)

print(E.issuperset({9}))

# Les sets ne prenent pas en considération les doubles , si la valeur éciste deja elle ne s'ajoute pas une 2eme fois

# EX5

# Check /mini-project
