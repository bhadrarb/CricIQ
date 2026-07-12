# 🏏 CricIQ

An end-to-end cricket analytics platform that predicts IPL match winners using Machine Learning and provides an interactive dashboard built with Streamlit.

---

## 📌 Overview

CricIQ uses historical IPL match data to predict the winner of a match based on factors such as team form, venue performance, toss details, home advantage, and head-to-head records. The application includes a user-friendly Streamlit interface for making predictions and viewing analytics.

---

## ✨ Features

- Predict IPL match winners using Machine Learning
- Interactive Streamlit web application
- Team-wise performance statistics
- Head-to-head analysis
- Home advantage calculation
- Venue-based win rate analysis
- Recent form analysis
- Comparison of multiple ML models

---

## 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly

### Web Framework
- Streamlit

### Model Serialization
- Joblib

---

## 📂 Project Structure

```
criciq/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── train.py
│   ├── predict.py
│   ├── best_model.pkl
│   └── target_encoder.pkl
│
├── utils/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── feature_calculator.py
│
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

- IPL Matches Dataset (2008–2024)
- Total Matches: **1090**
- Features include:
  - Season
  - Teams
  - Venue
  - Toss Winner
  - Toss Decision
  - Recent Form
  - Head-to-Head Win Rate
  - Venue Win Rate
  - Home Advantage

---

## ⚙️ Feature Engineering

The model uses historical information available before a match to generate predictive features.

- Recent form (last five matches)
- Head-to-head win rate
- Venue-specific win rate
- Home ground advantage

---

## 🤖 Machine Learning Models

The project compares multiple classification models.

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 50.92% |
| Random Forest | 50.92% |
| XGBoost | **52.29%** |

The best-performing model is automatically saved and used for prediction.

---

## 🖥 Application

The Streamlit dashboard allows users to:

- Select teams
- Select venue
- Select toss winner
- Select toss decision
- Predict match winner
- View prediction confidence
- View team statistics

---

## 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/criciq.git
```

Go into the project.

```bash
cd criciq
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app/app.py
```

---

## 📸 Screenshots

### Home Page

(Add Screenshot)

### Prediction Result

(Add Screenshot)

### Team Statistics

(Add Screenshot)

---

## 🔮 Future Improvements

- Live match data integration through cricket APIs
- Player performance analysis
- Win probability visualization
- Advanced model tuning
- Semantic match search
- Match history dashboard

---

## 👨‍💻 Author

**Bhadra R B**

GitHub: https://github.com/bhadrarb

LinkedIn: https://linkedin.com/in/bhadrarb