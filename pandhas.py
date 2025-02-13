import pandas as pd
import numpy as np

data = {
    "Name" : ["Pranjal","Jugnu", "Himanshu", "Deepanshu"],
    "Age" : [19,np.nan, 20,18],
    "location" : ["noida",np.nan, "delhi", "rewari"]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"] + 1

df["college"] = ["GU", np.nan,"DU", "BHU"]

print(df)