import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic_Cleaned.csv")

correlation = df[
    ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare", "CabinKnown"]
].corr()

print(correlation)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix of Titanic Variables")
plt.show()
