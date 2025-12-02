import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'Animals':['Chien','Chat','Lapin','Oiseau'], 'Effective' :[30,45,15,10]})

df.plot(kind='bar' , x='Animals' , y='Effective')

plt.show()
