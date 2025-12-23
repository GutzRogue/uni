import matplotlib.pyplot as plt
import pandas as pd

print("test")

df = pd.DataFrame(
    {
        "Classe (cm)": ["[150–154[", "[154–159[", "[159–167[", "[167–171["],
        "Amplitude": [4, 5, 8, 4],
        "Effectif": [6, 10, 14, 7],
    }
)

df["densités d’effectifs"] = df["Effectif"] / df["Amplitude"]

print(df)

df.plot(kind="bar", x="Classe (cm)", y="densités d’effectifs")

plt.show()
