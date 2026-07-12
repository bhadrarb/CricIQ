import sys
from pathlib import Path
import plotly.express as px
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd

from models.predict import predict_match
from utils.feature_calculator import get_features

st.set_page_config(
    page_title="CricIQ",
    layout="wide"
)

st.title("CricIQ")
st.subheader("Cricket Match Winner Prediction")

df = pd.read_csv("data/processed/features.csv")

teams = sorted(
    list(
        set(df["team1"]).union(set(df["team2"]))
    )
)

venues = sorted(df["venue"].unique())
seasons = sorted(df["season"].unique())

st.sidebar.header("Match Details")

season = st.sidebar.selectbox(
    "Season",
    seasons
)

team1 = st.sidebar.selectbox(
    "Team 1",
    teams
)

team2 = st.sidebar.selectbox(
    "Team 2",
    teams
)

if team1 == team2:
    st.error("Choose two different teams.")
    st.stop()

venue = st.sidebar.selectbox(
    "Venue",
    venues
)

toss_winner = st.sidebar.selectbox(
    "Toss Winner",
    [team1, team2]
)

toss_decision = st.sidebar.radio(
    "Toss Decision",
    ["bat", "field"]
)
predict = st.sidebar.button("Predict Winner")
if predict:

    (
        team1_recent,
        team2_recent,
        team1_h2h,
        team2_h2h,
        team1_venue,
        team2_venue,
        team1_home,
        team2_home
    ) = get_features(
        team1,
        team2,
        venue
    )

    winner, confidence = predict_match(
        season,
        team1,
        team2,
        venue,
        toss_winner,
        toss_decision,
        team1_recent,
        team2_recent,
        team1_h2h,
        team2_h2h,
        team1_venue,
        team2_venue,
        team1_home,
        team2_home
    )
    
    st.subheader("Match Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Team 1", team1)

    with col2:
        st.metric("Team 2", team2)

    st.header("Match Prediction")

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #00C853, #009624);
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        color: white;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.35);
        margin-bottom: 20px;
    ">

    <h3 style="margin:0;">Predicted Winner</h3>

    <h1 style="
        margin:15px 0;
        font-size:42px;
        font-weight:700;
    ">
    {winner}
    </h1>

    <h4 style="margin:0;">
    Winning Confidence: {float(confidence):.2f}%
    </h4>

    </div>
    """, unsafe_allow_html=True)

    st.progress(float(confidence) / 100)

    st.header("Team Statistics")
team1_matches = df[
    (df["team1"] == team1) |
    (df["team2"] == team1)
]

team1_played = len(team1_matches)

team1_wins = (team1_matches["winner"] == team1).sum()

team1_winrate = (
    team1_wins / team1_played * 100
    if team1_played > 0
    else 0
)
team2_matches = df[
    (df["team1"] == team2) |
    (df["team2"] == team2)
]

team2_played = len(team2_matches)

team2_wins = (team2_matches["winner"] == team2).sum()

team2_winrate = (
    team2_wins / team2_played * 100
    if team2_played > 0
    else 0
)
col1, col2 = st.columns(2)

with col1:

    st.subheader(team1)

    st.metric("Matches", team1_played)

    st.metric("Wins", team1_wins)

    st.metric(
        "Win %",
        f"{team1_winrate:.1f}%"
    )

with col2:

    st.subheader(team2)

    st.metric("Matches", team2_played)

    st.metric("Wins", team2_wins)

    st.metric(
        "Win %",
        f"{team2_winrate:.1f}%"
    )
st.header("Head-to-Head")
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
matches = len(h2h)

team1_wins = (h2h["winner"] == team1).sum()

team2_wins = (h2h["winner"] == team2).sum()
col1, col2, col3 = st.columns(3)

col1.metric(team1, team1_wins)

col2.metric(team2, team2_wins)

col3.metric("Matches", matches)
st.subheader("Recent Meetings")

st.dataframe(
    h2h[
        [
            "season",
            "date",
            "venue",
            "winner"
        ]
    ].sort_values(
        "date",
        ascending=False
    ).head(10)
)
st.header("Team Win Percentage")
all_teams = sorted(set(df["team1"]).union(set(df["team2"])))

stats = []

for team in all_teams:

    matches = df[
        (df["team1"] == team) |
        (df["team2"] == team)
    ]

    played = len(matches)

    wins = (matches["winner"] == team).sum()

    if played > 0:
        win_rate = wins / played * 100
    else:
        win_rate = 0

    stats.append({
        "Team": team,
        "Matches": played,
        "Wins": wins,
        "Win Rate": round(win_rate, 2)
    })

stats_df = pd.DataFrame(stats)

stats_df = stats_df.sort_values(
    "Win Rate",
    ascending=False
)
fig = px.bar(
    stats_df,
    x="Team",
    y="Win Rate",
    hover_data=["Matches", "Wins"],
    title="Overall Team Win Percentage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)