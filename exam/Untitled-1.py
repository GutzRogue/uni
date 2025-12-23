import pandas as pd

csv = pd.read_csv("ages.csv")

data = csv["Age"].dropna().astype(int).values
dic = {}

for i in data:
    i = int(
        i
    )  # <-- j'ai une erreur de typing dans mon éditeur si je n'ajoute pas cette ligne

    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# Age est deja sorted

df = pd.DataFrame(dic.items(), columns=["Age", "Eff"])

df["eff cumulative"] = df["Eff"].cumsum()

df["freq"] = df["Eff"] / df["Eff"].sum()

df["freq cumulative"] = df["freq"].cumsum()

N = df["Eff"].sum()
df_sorted = df.sort_values("Age").copy()
df_sorted["eff_cum"] = df_sorted["Eff"].cumsum()

moyenne = df["Age"].repeat(df["Eff"]).mean()

mode = df.loc[df["Eff"].max() == df["Eff"], "Age"]


def mediane(p):
    seuil = p * N
    return df_sorted.loc[df_sorted["eff_cum"] >= seuil, "Age"].iloc[0]


Q1 = mediane(0.25)
Q2 = mediane(0.50)
Q3 = mediane(0.75)

etendue = df["Age"].max() - df["Age"].min()

print("etendue:", etendue)
ecarts_types = ((df["Age"] - moyenne) ** 2 * df["Eff"]).sum()

moyenne_ponderee = (df["Age"] * df["Eff"]).sum() / df["Eff"].sum()

variance = ecarts_types / N
ecart_type = variance**0.5

print("Écart-type:", round(ecart_type, 2))

variance_ech = ecarts_types / (N - 1)
ecart_type_ech = variance_ech**0.5

print("Écart-type corriger:", round(ecart_type_ech, 2))
