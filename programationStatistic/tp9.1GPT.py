import matplotlib.pyplot as plt
import seaborn as sns

data = [149, 153, 157, 159, 160, 162, 165, 167, 168, 171]

plt.hist(data, bins=5, density=True, alpha=0.4, edgecolor="black")

sns.kdeplot(x=data)

plt.xlabel("Taille (cm)")
plt.ylabel("Densité")
plt.title("Histogramme + KDE")
plt.show()
