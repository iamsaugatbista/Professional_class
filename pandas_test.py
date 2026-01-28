# Pandas EXample
import pandas as pd

data = {
    "Name":["A","B","C"],
    "Marks":[80,70,90]
}

df = pd.DataFrame(data)
print(df)
print("\nDescription:\n", df.describe())


# Matplotlib Example
import matplotlib.pyplot as plt

marks = [80,70,90,85,60]
plt.plot(marks)
plt.title("Students Marks Trend")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()