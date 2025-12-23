import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Etudiant": ["A", "B", "C", "D", "E", "F"],
    "Heures_etude": [2, 4, 5, 7, 8, 9],
    "Note": [40, 55, 60, 75, 90, 92]
})


plt.scatter(x=df["Heures_etude"], y=df["Note"])

plt.show()
