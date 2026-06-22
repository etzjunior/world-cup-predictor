import pandas as pd

df = pd.read_csv("data/raw/results.csv")

print("Shape:")
print(df.shape)

print("\nDate Range:")
print(df["date"].min())
print(df["date"].max())

print("\nUnique Teams:")
teams = set(df["home_team"]).union(set(df["away_team"]))
print(len(teams))

print("\nTop 10 Tournaments:")
print(df["tournament"].value_counts().head(10))

print("\nShape:")
print(df.shape)

print("\nDate Range:")
print(df["date"].min())
print(df["date"].max())