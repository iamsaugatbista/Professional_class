import pandas as pd

# Create a DataFrame from a list of dictionaries
data = [{'Name':'Alice','Age':25}, {'Name':'Bob','Age':30}, {'Name':'Charlie','Age':35}]
df = pd.DataFrame(data)

# Filter rows where Age > 28
filtered = df[df['Age'] > 28]

print("Original DataFrame:\n", df)
print("\nFiltered (Age > 28):\n", filtered)

