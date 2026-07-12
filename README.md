# CricIQ

CricIQ is a machine learning-based cricket analytics platform that predicts IPL match winners using historical match data. The application provides an interactive Streamlit dashboard for match prediction and team analytics.

---
---

## Features
Predict IPL match winners
- Team performance statistics
- Head-to-head analysis
- Recent form and venue-based feature engineering
- Interactive Streamlit dashboard
- Comparison of multiple ML models
---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Plotly
- Joblib
  
## Dataset

- IPL Matches Dataset (2008–2024)
- 1090 historical matches

### Features Used

- Season
- Teams
- Venue
- Toss Winner
- Toss Decision
- Recent Form
- Head-to-Head Win Rate
- Venue Win Rate
- Home Advantage

## Model Performance

model accuracy

Logistic Regression - 50.92% 
Random Forest - 50.92% 
XGBoost - **52.29%** 

The best-performing model is automatically saved and used for prediction.


## Project Structure

```text
criciq/
│── app/
│── data/
│── models/
│── utils/
│── requirements.txt
│── README.md
└── .gitignore
## running the project
git clone https://github.com/YOUR_USERNAME/criciq.git
cd criciq
pip install -r requirements.txt

streamlit run app/app.py
```

## 📸 Screenshots

### Home Page

(assets/home.png)

### Prediction Result

(assets/prediction.png)

---

## Future Improvements
- Hyperparameter tuning
- Live cricket API integration
- Player performance analytics
- Win probability visualization
---

## Author

**Bhadra R B**

GitHub: https://github.com/bhadrarb

LinkedIn: https://linkedin.com/in/bhadrarb
