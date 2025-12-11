import pandas as pd 
import matplotlib.pyplot as plt

data = {
        "Classes" : ["A" , "A" , "A" , "B" , "B" , "B"],
        "Notes" : [12 , 15 , 18 ,10 ,14,16],
        "Sexe" : ["M" , "F" , "M" , "F" , "M" , "F"]
        }

df = pd.DataFrame(data)

# df["Sexe"].value_counts().plot(kind="bar")

# plt.show()

df["Notes"].plot(kind='hist', bins = 5 )

plt.show()

print(df)


