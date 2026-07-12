import pandas as pd

df = pd.read_csv(
    "data/processed/clean_matches.csv",
    parse_dates=["date"]
)

df["team1_recent_form"] = 0
df["team2_recent_form"] = 0

df["team1_h2h_winrate"] = 0.0
df["team2_h2h_winrate"] = 0.0

df["team1_venue_winrate"] = 0.0
df["team2_venue_winrate"] = 0.0

df["team1_home"] = 0
df["team2_home"] = 0
home_grounds = {
    "Mumbai Indians": "Wankhede Stadium",
    "Chennai Super Kings": "MA Chidambaram Stadium",
    "Royal Challengers Bangalore": "M Chinnaswamy Stadium",
    "Kolkata Knight Riders": "Eden Gardens",
    "Delhi Capitals": "Arun Jaitley Stadium",
    "Punjab Kings": "Punjab Cricket Association Stadium",
    "Rajasthan Royals": "Sawai Mansingh Stadium",
    "Sunrisers Hyderabad": "Rajiv Gandhi International Stadium",
    "Lucknow Super Giants": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium",
    "Gujarat Titans": "Narendra Modi Stadium"
}
def recent_form(team, current_date, matches=5):
    """Return the number of wins in the team's last five matches."""
    previous_matches = df[
        (
            (df["team1"] == team) |
            (df["team2"] == team)
        ) &
        (df["date"] < current_date)
    ]

    previous_matches = previous_matches.sort_values(
        "date",
        ascending=False
    ).head(matches)

    wins = (previous_matches["winner"] == team).sum()

    return wins


def head_to_head(team1, team2, current_date):
    """Return historical head-to-head win rates before the given date."""
    previous = df[
        (
            (
                (df["team1"] == team1) &
                (df["team2"] == team2)
            )
            |
            (
                (df["team1"] == team2) &
                (df["team2"] == team1)
            )
        )
        &
        (df["date"] < current_date)
    ]

    total_matches = len(previous)

    if total_matches == 0:
        return 0.5, 0.5

    team1_wins = (previous["winner"] == team1).sum()
    team2_wins = (previous["winner"] == team2).sum()

    return (
        team1_wins / total_matches,
        team2_wins / total_matches
    )


def venue_win_rate(team, venue, current_date):
    """Return the team's historical win rate at the venue."""
    previous = df[
        (
            (
                (df["team1"] == team) |
                (df["team2"] == team)
            )
            &
            (df["venue"] == venue)
            &
            (df["date"] < current_date)
        )
    ]

    total = len(previous)

    if total == 0:
        return 0.5

    wins = (previous["winner"] == team).sum()

    return wins / total
for idx, row in df.iterrows():

    venue = row["venue"]

    if home_grounds.get(row["team1"]) == venue:
        df.at[idx, "team1_home"] = 1

    if home_grounds.get(row["team2"]) == venue:
        df.at[idx, "team2_home"] = 1
    
    df.at[idx, "team1_recent_form"] = recent_form(
        row["team1"],
        row["date"]
    )
    team1_rate, team2_rate = head_to_head(
        row["team1"],
        row["team2"],
        row["date"]
    )

    df.at[idx, "team1_h2h_winrate"] = team1_rate
    df.at[idx, "team2_h2h_winrate"] = team2_rate
    df.at[idx, "team2_recent_form"] = recent_form(
        row["team2"],
        row["date"]
    )
    df.at[idx, "team1_venue_winrate"] = venue_win_rate(
        row["team1"],
        row["venue"],
        row["date"]
    )

    df.at[idx, "team2_venue_winrate"] = venue_win_rate(
        row["team2"],
        row["venue"],
        row["date"]
    )
  
df.to_csv(
    "data/processed/features.csv",
    index=False
)

print("Feature engineering complete.")