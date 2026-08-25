# ============================================================
# TITANIC DATA ANALYSIS - VISUALIZATIONS
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("Titanic_Cleaned.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 2. CREATE IMAGES FOLDER
# ------------------------------------------------------------

os.makedirs("images", exist_ok=True)

print("\nImages folder ready!")


# ------------------------------------------------------------
# 3. SURVIVAL COUNT
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.countplot(data=df, x="Survived")

plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("images/survival_count.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 4. SURVIVAL RATE BY GENDER
# ------------------------------------------------------------

gender_survival = (
    df.groupby("Sex")["Survived"]
    .mean()
    .reset_index()
)

gender_survival["SurvivalRate"] = gender_survival["Survived"] * 100

plt.figure(figsize=(8, 6))

sns.barplot(
    data=gender_survival,
    x="Sex",
    y="SurvivalRate"
)

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)

for i, value in enumerate(gender_survival["SurvivalRate"]):
    plt.text(
        i,
        value + 2,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("images/survival_by_gender.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 5. SURVIVAL RATE BY PASSENGER CLASS
# ------------------------------------------------------------

class_survival = (
    df.groupby("Pclass")["Survived"]
    .mean()
    .reset_index()
)

class_survival["SurvivalRate"] = class_survival["Survived"] * 100

plt.figure(figsize=(8, 6))

sns.barplot(
    data=class_survival,
    x="Pclass",
    y="SurvivalRate"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)

for i, value in enumerate(class_survival["SurvivalRate"]):
    plt.text(
        i,
        value + 2,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("images/survival_by_class.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 6. SURVIVAL RATE BY AGE GROUP
# ------------------------------------------------------------

# Create age groups if AgeGroup does not already exist
if "AgeGroup" not in df.columns:

    def create_age_group(age):

        if age < 13:
            return "Child"

        elif age < 20:
            return "Teen"

        elif age < 30:
            return "Young Adult"

        elif age < 60:
            return "Adult"

        else:
            return "Senior"

    df["AgeGroup"] = df["Age"].apply(create_age_group)


age_survival = (
    df.groupby("AgeGroup")["Survived"]
    .mean()
    .reset_index()
)

age_survival["SurvivalRate"] = age_survival["Survived"] * 100

age_order = [
    "Child",
    "Teen",
    "Young Adult",
    "Adult",
    "Senior"
]

plt.figure(figsize=(9, 6))

sns.barplot(
    data=age_survival,
    x="AgeGroup",
    y="SurvivalRate",
    order=age_order
)

plt.title("Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)

for i, group in enumerate(age_order):

    value = age_survival[
        age_survival["AgeGroup"] == group
    ]["SurvivalRate"]

    if len(value) > 0:
        plt.text(
            i,
            value.iloc[0] + 2,
            f"{value.iloc[0]:.1f}%",
            ha="center"
        )

plt.tight_layout()
plt.savefig("images/survival_by_age_group.png", dpi=300, bbox_inches="tight")
plt.show()


# ------------------------------------------------------------
# 7. SURVIVAL RATE BY EMBARKED PORT
# ------------------------------------------------------------

if "Embarked" in df.columns:

    embarked_survival = (
        df.groupby("Embarked")["Survived"]
        .mean()
        .reset_index()
    )

    embarked_survival["SurvivalRate"] = (
        embarked_survival["Survived"] * 100
    )

    plt.figure(figsize=(8, 6))

    sns.barplot(
        data=embarked_survival,
        x="Embarked",
        y="SurvivalRate"
    )

    plt.title("Survival Rate by Embarkation Port")
    plt.xlabel("Embarkation Port")
    plt.ylabel("Survival Rate (%)")
    plt.ylim(0, 100)

    for i, value in enumerate(
        embarked_survival["SurvivalRate"]
    ):
        plt.text(
            i,
            value + 2,
            f"{value:.1f}%",
            ha="center"
        )

    plt.tight_layout()

    plt.savefig(
        "images/survival_by_embarked.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ------------------------------------------------------------
# 8. FARE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.histplot(
    data=df,
    x="Fare",
    bins=30,
    kde=True
)

plt.title("Distribution of Passenger Fares")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "images/fare_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# 9. AGE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.histplot(
    data=df,
    x="Age",
    bins=30,
    kde=True
)

plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "images/age_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# 10. SURVIVAL BY GENDER AND CLASS
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.barplot(
    data=df,
    x="Pclass",
    y="Survived",
    hue="Sex"
)

plt.title("Survival Rate by Passenger Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.tight_layout()

plt.savefig(
    "images/survival_class_gender.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# 11. CORRELATION HEATMAP
# ------------------------------------------------------------

numeric_columns = [
    "Survived",
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

# Add CabinKnown if available
if "CabinKnown" in df.columns:
    numeric_columns.append("CabinKnown")

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix of Titanic Variables")

plt.tight_layout()

plt.savefig(
    "images/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# 12. FINAL MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 50)
print("ANALYSIS COMPLETE!")
print("=" * 50)

print("\nAll visualization images have been saved inside:")
print("images/")

print("\nGenerated files:")

for file in os.listdir("images"):
    print("-", file)
    
