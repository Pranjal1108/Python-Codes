import pandas as pdf
data = {
    "name" : ["Pranjal", "Himanshu", "Deepanshu"],
    "age" : [19, 20, 18],
    "location" : ["Noida", "Delhi", ]
}

df = pdf.DataFrame(data)
print(df)