import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
df = pd.read_csv("data/processed/features.csv")

features = [
        "season",

    "team1",
    "team2",

    "venue",

    "toss_winner",
    "toss_decision",

    "team1_recent_form",
    "team2_recent_form",

    "team1_h2h_winrate",
    "team2_h2h_winrate",

    "team1_venue_winrate",
    "team2_venue_winrate",

    "team1_home",
    "team2_home"
]
target = "winner"
categorical_features = [
    "season",

    "team1",

    "team2",

    "venue",

    "toss_winner",

    "toss_decision"

]
numeric_features = [
    "team1_recent_form",
    "team2_recent_form",

    "team1_h2h_winrate",
    "team2_h2h_winrate",

    "team1_venue_winrate",
    "team2_venue_winrate",

    "team1_home",
    "team2_home"

]
X = df[features].copy()

y = df[target].copy()


target_encoder = LabelEncoder()

y = target_encoder.fit_transform(y)

joblib.dump(
    target_encoder,
    "models/target_encoder.pkl"
)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numeric_features
        )
    ]
)
models = {
    "Logistic Regression": Pipeline([
        ("prep", preprocessor),
        ("model", LogisticRegression(max_iter=1000,random_state=42))
    ]),

    "Random Forest": Pipeline([
        ("prep", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=300,
            random_state=42
        ))
    ]),

    "XGBoost": Pipeline([
        ("prep", preprocessor),
        ("model", XGBClassifier(
                n_estimators=300,
                learning_rate=0.05,
                max_depth=6,
                random_state=42,
                eval_metric="mlogloss"
))
    ])
}
best_model = None
best_accuracy = 0

for name, model in models.items():

    print("=" * 50)
    print(name)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report")
    print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

joblib.dump(
    best_model,
    "models/best_model.pkl"
)

print(f"\nBest Accuracy: {best_accuracy:.4f}")
print("Best model saved.")