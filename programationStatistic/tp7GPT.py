import matplotlib.pyplot as plt
import pandas as pd

sizes = [147, 150, 152, 154, 155, 158, 160, 161, 162, 165, 167, 168, 169, 171, 172]

n = 147

data = {}

while n < 172:
    count = 0

    for i in sizes:
        if n <= i < n + 4 or (n == 168 and n <= i <= n + 4):
            count += 1

    data[f"[,{n},{n+4},["] = count;
    n += 4

df = pd.DataFrame(list(data.items()),columns=['grps','effs'])

df.plot(kind="bar" , x="grps" , y="effs" )

plt.show()

print(df)
