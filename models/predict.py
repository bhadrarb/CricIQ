from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "best_model.pkl")
target_encoder = joblib.load(BASE_DIR / "target_encoder.pkl")


def predict_match(
    season,
    team1,
    team2,
    venue,
    toss_winner,
    toss_decision,
    team1_recent_form,
    team2_recent_form,
    team1_h2h_winrate,
    team2_h2h_winrate,
    team1_venue_winrate,
    team2_venue_winrate,
    team1_home,
    team2_home
):

    data = pd.DataFrame([{
        "season": season,
        "team1": team1,
        "team2": team2,
        "venue": venue,
        "toss_winner": toss_winner,
        "toss_decision": toss_decision,
        "team1_recent_form": team1_recent_form,
        "team2_recent_form": team2_recent_form,
        "team1_h2h_winrate": team1_h2h_winrate,
        "team2_h2h_winrate": team2_h2h_winrate,
        "team1_venue_winrate": team1_venue_winrate,
        "team2_venue_winrate": team2_venue_winrate,
        "team1_home": team1_home,
        "team2_home": team2_home
    }])

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    winner = target_encoder.inverse_transform(prediction)[0]

    confidence = round(float(probability.max() * 100), 2)

    return winner, confidence