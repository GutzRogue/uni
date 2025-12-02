import pandas as pd
import matplotlib.pyplot as plt

notes = [10, 12, 8, 14, 10, 16, 12, 12, 8, 10, 18, 14, 6, 10, 12]

notes.sort()

dict = {}

for i in notes:
    if(i in dict):
        dict[i] += 1
    else:
        dict[i] = 1

df = pd.DataFrame(list(dict.items()), columns=['data', 'effective'])

df['effective_cumulé'] = df['effective'].cumsum() 

df["frequancy"] = df['effective'] / df['effective'].sum()

df['frequancy_cum'] = df['effective_cumulé']/df['effective'].sum()

df.plot(x='data' , y='effective')

plt.title("Notes de class")

plt.show()
