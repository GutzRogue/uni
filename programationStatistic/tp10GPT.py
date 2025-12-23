import pandas as pd
from datasets import load_dataset, Dataset
from typing import cast
import math

ds = cast(Dataset, load_dataset("scikit-learn/tips", split="train"))
df = cast(pd.DataFrame, ds.with_format("pandas")[:])

df.dropna()

days = df["day"]

data = {}

for i in days:
    if i in data:
        data[i] += 1
    else:
        data[i] =1

d1 = pd.DataFrame(list(data.items()) , columns=["Days" , "Eff ni"])

d1["EffCum Ni"] = d1["Eff ni"].cumsum()

d1["freq fi"] =  d1["Eff ni"]/ d1["Eff ni"].sum()

d1["freqCum Fi"] = d1["freq fi"].cumsum() 

print(df["total_bill"])

nb_class = int(1+math.log2(len(df["total_bill"]))) 

print(nb_class)





