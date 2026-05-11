import pandas as pd

df = pd.read_csv("data/transactions.csv")

df["date"] = pd.to_datetime(df["date"])
df["description"] = df["description"].str.lower().str.strip()
df["amount"] = pd.to_numeric(df["amount"])
df["type"] = df["type"].str.lower().str.strip()

df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.day_name()
df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

print(df)
print("\nTotal income:", df[df["type"] == "income"]["amount"].sum())
print("Total expense:", df[df["type"] == "expense"]["amount"].sum())