import matplotlib.pyplot as plt
import pandas as pd
import math

salaires = [18000, 19000, 19500, 20000, 21000, 22500, 23000,
23500, 24000, 26000, 27500, 29000, 30000, 31000]

nb_class = round(2.5 * math.pow(len(salaires) , 1/4))

minim = min(salaires)
maxim = max(salaires)

size = maxim - minim

ampli = size/nb_class

debut = minim
bornes = []

di = {}

for i in range(nb_class):
    fin = round(debut + ampli)
    if( fin > maxim):
        fin = round(maxim)
    bornes.append((debut,fin))    
    key =f"{debut},{fin}"
    di[key] = 0 
    debut = fin

for i in salaires:
    for (a,b) in bornes:
        if a<= i < b or (b==maxim and a <= i <= b):
            key =f"{a},{b}"
            di[key] += 1
            

df= pd.DataFrame(list(di.items()), columns=["salaires","eff"])

df.plot(kind="bar" ,x="salaires" , y="eff")

plt.show()



print(df)
