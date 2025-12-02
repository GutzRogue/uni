import math
import pandas as pd
import matplotlib.pyplot as plt
#EX1

salaires = [2400, 2700, 3000, 3100, 2950, 4100, 3800, 3600, 2500, 3300,
2600, 2800, 3400, 3550, 2900, 4100, 4200, 4600, 2300, 2800,
3200, 3000, 3600, 3900, 4500]

nombre_de_classes = round(2.5 * math.pow(len(salaires) , 1/4))

largeur = 400

debut = min(salaires)
bornes = []
maximal = max(salaires)

di = {}

for i in range(nombre_de_classes):
    fin = debut + largeur
    if fin > maximal:
        fin = maximal
    bornes.append((debut,fin))
    key = f"{debut},{fin}"
    di[key] = 0
    debut = fin

for i in salaires:
    for  (a,b) in bornes:
        if a <= i < b or ( b == maximal and a <= i <= b):
            key = f"{a},{b}"
            di[key] += 1

:
df = pd.DataFrame(list(di.items()) , columns = ["salaires" , "effectives"])

df['freq'] = df['effectives'] / df["effectives"].sum()

df.plot(kind='bar', x="salaires" , y='effectives')


