import pandas as pd
temp = range(0,50)
data = {
    "Winter" : ["Wheat", "Mustard", "Barley"],
    "Monsoon" : ["Rice", "Maize", "Cotton"],
    "Summer" : ["Watermelon", "Cucumber", "Muskmelon"]
}
df = pd.DataFrame(data)
print(df)