# 🏏 IPL Data Analysis Dashboard with Live Score Prediction

## 📌 Project Overview

This project focuses on analyzing Indian Premier League (IPL) data and building an interactive dashboard using Streamlit. It provides insights into team performance, player statistics, and match trends. Additionally, it includes a live score prediction model that estimates the final score based on current match conditions.

---

## 🚀 Features

* 📊 Team Performance Analysis
* 🏏 Player Statistics Visualization
* 📈 Season-wise Trends
* 🎯 Live Score Prediction Model
* 🖥 Interactive Dashboard using Streamlit

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Libraries Used:** Pandas, NumPy, Matplotlib
* **Framework:** Streamlit
* **Machine Learning:** Basic Regression Model
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
ipl-data-analysis/
│
├── app.py
├── requirements.txt
├── data/
│   ├── matches.csv
│   └── deliveries.csv
├── assets/
│   └── ipl_logo.png
├── screenshots/
│   └── dashboard.png
└── README.md
```

---

## 📊 Dataset Information

The project uses IPL datasets:

* **matches.csv:** Contains match-level data such as teams, results, venues, and seasons
* **deliveries.csv:** Contains ball-by-ball data including runs, wickets, and player performance

---

## 🧹 Data Preprocessing

* Handling missing values
* Removing duplicate records
* Filtering relevant data
* Feature creation (e.g., run rate)

---

## 🤖 Machine Learning Model

A basic regression-based model is used to predict the final score of a match.

### 🔍 Input Features:

* Overs completed
* Current runs
* Wickets lost
* Runs in last 5 overs
* Wickets in last 5 overs

### 📤 Output:

* Predicted final score

---

## 🖥 User Interface (Streamlit)

The dashboard includes:

* Home Section
* Team Analysis
* Player Analysis
* Visualizations
* Live Score Predictor

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/ipl-data-analysis.git
cd ipl-data-analysis
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Application

```bash
streamlit run app.py
```
---

## 🌐 Deployment

The project can be deployed using Streamlit Cloud for online access.

---

## ⚠️ Challenges Faced

* Handling missing and inconsistent data
* Managing large datasets
* Designing an interactive UI
* Implementing prediction logic

---

## 🚀 Future Scope

* Integration of real-time IPL data
* Advanced machine learning models
* More interactive visualizations
* Deployment for public access

---

## 👨‍💻 Author

**Utkarsh Tiwari**
BCA Student

---

## ⭐ Conclusion

This project demonstrates the practical application of data analysis, visualization, and machine learning in sports analytics using IPL data.

---
