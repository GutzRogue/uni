import matplotlib.pyplot as plt

notes = [8, 10, 11, 12, 13, 13, 14, 15, 17, 18, 20, 21, 25]
notes.sort()


def calcMed(a, b):
    arr = notes[a : b + 1]  # b inclus
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid - 1]) / 2
    else:
        return arr[mid]


n = len(notes)
mid = n // 2

# médiane globale
Q2 = calcMed(0, n - 1)

if n % 2 == 1:
    # n impair → on enlève la médiane du milieu
    Q1 = calcMed(0, mid - 1)  # bas : 0 .. mid-1
    Q3 = calcMed(mid + 1, n - 1)  # haut : mid+1 .. n-1
else:
    # n pair → on coupe en deux moitiés égales
    Q1 = calcMed(0, mid - 1)  # bas : 0 .. mid-1
    Q3 = calcMed(mid, n - 1)  # haut : mid .. n-1

IQR = Q3 - Q1

bornesLow = Q1 - (1.5 * IQR)
bornesHigh = Q3 + (1.5 * IQR)

plt.boxplot(notes, vert=True, showmeans=True)

plt.show()

print("Done")
