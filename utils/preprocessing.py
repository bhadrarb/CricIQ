import pandas as pd
import os

# -----------------------------
# Load Dataset
# -----------------------------
DATA_PATH = "data/raw/matches.csv"

df = pd.read_csv(DATA_PATH)

print("Original Shape:", df.shape)

# -----------------------------
# Remove Duplicate Matches
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Remove Matches With No Winner
# -----------------------------
df = df[df["winner"].notna()]

# -----------------------------
# Remove No Result Matches
# -----------------------------
df = df[df["result"] != "no result"]

# -----------------------------
# Standardize Team Names
# -----------------------------
team_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiant": "Rising Pune Supergiants"
}

for column in ["team1", "team2", "toss_winner", "winner"]:
    df[column] = df[column].replace(team_mapping)

# -----------------------------
# Convert Date
# -----------------------------
df["date"] = pd.to_datetime(
    df["date"],
    dayfirst=True,
    errors="coerce"
)

# Remove rows with invalid dates
df = df[df["date"].notna()]

# Sort chronologically
df = df.sort_values("date").reset_index(drop=True)

print("Cleaned Shape:", df.shape)

# -----------------------------
# Save Clean Dataset
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

OUTPUT_PATH = "data/processed/clean_matches.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved cleaned dataset to {OUTPUT_PATH}")