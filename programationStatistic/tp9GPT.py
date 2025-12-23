import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Age = [12, 14, 40, 35, 26, 30, 30, 50, 75, 50, 30, 45, 25, 55, 28, 25, 50, 40, 25, 35]

Loisir = ["S", "S", "C", "C", "S", "T", "T", "L","L", "L", "T", "C", "C", "C", "S", "L", "L", "C", "T", "T"]

Age.sort()

data = {}

for i in Age:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

df = pd.DataFrame(list(data.items()) , columns=["xi" , "ni"])

df["Ni"] = df["ni"].cumsum()

df["fi"] = df["ni"] / df["ni"].sum()

df["Fi"] = df["fi"].cumsum()

Moyen = sum(Age) / len(Age)

Median = np.median(Age)

print(Median)

