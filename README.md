# ✈️ SkyRate — Airline Passenger Satisfaction Intelligence

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![XGBoost](https://img.shields.io/badge/XGBoost-90%25%20Accuracy-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

> 🎓 **Capstone Project — PGP Data Science & Generative AI | Great Learning | 2026**

---

## 🌐 Live Demo

👉 **[Launch SkyRate App](https://skyrate-airline-customer-satisfaction-xedjrcsbryf7jes98tqqlb.streamlit.app/)**
---

## 📌 Project Overview

**SkyRate** is a full-stack AI-powered airline passenger satisfaction prediction system. It combines a **conversational chatbot** for passenger feedback collection with a **real-time analytics dashboard** for airline operations teams.

The system uses a **2-Stage Machine Learning architecture** — Stage 1 predicts satisfaction from pre-flight experience, while Stage 2 analyzes in-flight service quality — both powered by **XGBoost** achieving **90-92% accuracy**.

> 💡 **Business Problem:** Airlines struggle to identify dissatisfied passengers in real-time. SkyRate solves this by predicting satisfaction immediately after pre-flight check-in, enabling proactive service recovery before the flight departs.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🤖 **AI Chatbot** | 7-step conversational feedback collection |
| 📊 **Live Dashboard** | Real-time KPIs, charts, and passenger records |
| 🔮 **Instant Prediction** | XGBoost predicts satisfaction in milliseconds |
| 🎨 **Custom Dark UI** | Professional airline-grade interface |
| 📥 **CSV Export** | Download all passenger data instantly |
| 🔍 **Smart Filtering** | Search and filter by PNR, seat, satisfaction |

---

## 🧠 ML Architecture — 2-Stage Model

```
┌─────────────────────────────────────────────────────┐
│                  STAGE 1 (Pre-Flight)                │
│  Demographics + Booking + Airport Experience         │
│  → XGBoost → 90.3% Accuracy | 92.7% Recall         │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                  STAGE 2 (In-Flight)                 │
│  WiFi + Entertainment + Comfort + Food + Crew        │
│  → XGBoost → 92.0% Accuracy | 93.7% Recall         │
└─────────────────────────────────────────────────────┘
```

### Why 2 Stages?
- **Stage 1** runs at check-in — early warning system for ground staff
- **Stage 2** runs post-flight — identifies in-flight service gaps
- Prevents **data leakage** between pre-flight and in-flight features
- Enables **targeted intervention** at each journey stage

---

## 📊 Model Performance

### Stage 1 — Pre-Flight Prediction

| Model | Accuracy | Recall |
|---|---|---|
| Logistic Regression | 83% | 80% |
| Decision Tree | 86% | 84% |
| Random Forest | 89% | 88% |
| SVM | 82% | 79% |
| AdaBoost | 88% | 87% |
| **XGBoost ✅** | **90.3%** | **92.7%** |

### Stage 2 — In-Flight Prediction

| Model | Accuracy | Recall |
|---|---|---|
| Logistic Regression | 85% | 82% |
| Decision Tree | 88% | 86% |
| Random Forest | 91% | 90% |
| SVM | 84% | 81% |
| AdaBoost | 89% | 88% |
| **XGBoost ✅** | **92.0%** | **93.7%** |

> 📌 **Why Recall over Accuracy?** Missing a dissatisfied passenger costs the airline more than a false alarm. Recall ensures maximum detection of unhappy customers.

---

## 🔑 Key Insights

```
Stage 1 — Pre-Flight Drivers:
🏆 Online Boarding — strongest predictor of satisfaction
✈️  Type of Travel (Business) — business travelers demand higher service
📱 Ease of Online Booking — digital experience sets expectations

Stage 2 — In-Flight Drivers:
📶 In-flight WiFi (29%) — #1 satisfaction driver
🎬 In-flight Entertainment (22%) — critical for long-haul
💺 Leg Room Service (11%) — physical comfort matters
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **ML Models** | XGBoost, Scikit-learn, Pipeline |
| **Explainability** | SHAP, Feature Importance |
| **Clustering** | KMeans + PCA |
| **Frontend** | Streamlit + Custom CSS |
| **Charts** | Plotly |
| **Data** | Pandas, NumPy |
| **Deployment** | Streamlit Cloud + GitHub Codespaces |

---

## 🔄 How It Works

```
Passenger → SkyBot Chatbot (7 steps)
                ↓
    Ratings collected (booking, check-in, boarding, gate)
                ↓
    Stage-1 XGBoost predicts satisfaction (hidden from passenger)
                ↓
    Result stored → Dashboard updates instantly
                ↓
    Airline team sees: KPIs + Charts + Passenger Table
```

---

## 📁 Project Structure

```
SkyRate-Airline-Customer-Satisfaction/
│
├── 🐍 app.py                    ← Main entry point (tabs + CSS)
├── 🤖 model.py                  ← XGBoost Stage-1 pipeline
├── 📋 requirements.txt          ← Dependencies
├── 🚫 .gitignore
│
├── 📂 pages/
│   ├── 💬 chatbot.py            ← 7-step passenger feedback bot
│   └── 📊 dashboard.py          ← Live airline analytics dashboard
│
├── 📂 .devcontainer/
│   └── devcontainer.json        ← GitHub Codespaces config
│
├── 📓 Stage1_Notebook.ipynb     ← Pre-flight ML analysis
├── 📓 Stage2_Notebook.ipynb     ← In-flight ML analysis
│
└── 📄 README.md
```
## 🧠 What I Learned

- Building **end-to-end ML pipelines** with no data leakage
- **2-Stage model architecture** for sequential prediction problems
- **SHAP explainability** for model interpretability
- **KMeans + PCA** for customer segmentation
- Deploying ML models as **production Streamlit apps**
- **Custom UI design** with CSS in Streamlit
- Real-time **state management** in multi-page apps

---

## 👨‍💻 Author

**Kiran U**

BCA Graduate | PGP in Data Science & Generative AI — Great Learning, Bangalore

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/kiran-u-471818325/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/KIRAN4003)
[![App](https://skyrate-airline-customer-satisfaction-xedjrcsbryf7jes98tqqlb.streamlit.app/)

---

⭐ **If you found this project useful, please give it a star!**
