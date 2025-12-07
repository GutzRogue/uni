import gestion_notes as gn

n = [12, 9, 15, 7]

new_n = float(input("Donner la nouvelle note\n"))

# La on teste si le user n'essay pas de nous truquer avec une note negative ou +20

while new_n < 0 or new_n > 20:
    new_n = float(input("La note doit etre comprise entre 0 et 20\n"))

# On prend juste 2 notes apres la virgule car c'est une note

new_n = round(new_n, 2)


gn.ajouter_note(n, new_n)

a = gn.moyenne(n)

b = gn.note_max(n)

c = gn.est_reussi(a)

print("Moyenne : ", a)

print("Note maximal :", b)

print("Avez vous passer? ", c)

# EX3:

# Un module est un fichier Python qui contient des fonctions. Il permet de :
# • réutiliser du code dans plusieurs programmes
# • clarifier l’organisation
# • éviter la duplication de code
