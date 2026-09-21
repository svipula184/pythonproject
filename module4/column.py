import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya"],
    "Age": [20, 21, 20],
    "Branch": ["CSE", "ISE", "ECE"],
    "CGPA": [8.5, 7.8, 9.1]
}

df = pd.DataFrame(data)

print(df.columns)