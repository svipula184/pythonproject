import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Anu", "Rahul"],
    "Python": [85, 78, 92, 74, 88, 81],
    "DAA": [80, 75, 89, 70, 85, 79],
    "CGPA": [8.5, 7.8, 9.1, 7.2, 8.8, 8.0]
}

df = pd.DataFrame(data)

print(df.tail())