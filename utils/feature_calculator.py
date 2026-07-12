import pandas as pd

df = pd.read_csv("data/processed/features.csv")


def get_features(team1, team2, venue):

    # Team 1 recent form
    t1 = df[df["team1"] == team1]

    if len(t1):
        team1_recent = t1.iloc[-1]["team1_recent_form"]
    else:
        team1_recent = 0

    # Team 2 recent form
    t2 = df[df["team2"] == team2]

    if len(t2):
        team2_recent = t2.iloc[-1]["team2_recent_form"]
    else:
        team2_recent = 0

    # Head to head
    h2h = df[
        (
            (df["team1"] == team1) &
            (df["team2"] == team2)
        )
        |
        (
            (df["team1"] == team2) &
            (df["team2"] == team1)
        )
    ]

    if len(h2h):
        last = h2h.iloc[-1]
        team1_h2h = last["team1_h2h_winrate"]
        team2_h2h = last["team2_h2h_winrate"]
    else:
        team1_h2h = 0.5
        team2_h2h = 0.5

    # Venue
    v = df[df["venue"] == venue]

    if len(v):
        last = v.iloc[-1]
        team1_venue = last["team1_venue_winrate"]
        team2_venue = last["team2_venue_winrate"]
    else:
        team1_venue = 0.5
        team2_venue = 0.5

    # Home grounds
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

    team1_home = int(home_grounds.get(team1) == venue)
    team2_home = int(home_grounds.get(team2) == venue)

    return (
        team1_recent,
        team2_recent,
        team1_h2h,
        team2_h2h,
        team1_venue,
        team2_venue,
        team1_home,
        team2_home
    )