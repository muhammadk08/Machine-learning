import pandas as pd

x = {
    "Name": ["Rose", "John", "Jane", "Mary"],

    "ID": [1, 2, 3, 4],

    "Department": ["Architect Group", "Software Group", "Design Team", "Infrastructure"],

    "Salary": [100000, 80000, 50000, 60000]
}

df = pd.DataFrame(x)
print(df)

x = df[["ID"]]
print(x)
print(type(x))

print(df.iloc[0, 0])

print(df.iloc[1:3, 0:3])