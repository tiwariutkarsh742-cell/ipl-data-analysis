import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 
from PIL import Image 

st.set_page_config(page_title="IPL Dashboard", page_icon="🏏", layout="wide")

# ---------- Load Data ----------
@st.cache_data
def load_data():
    matches = pd.read_csv("matches.csv")
    deliveries = pd.read_csv("deliveries.csv")
    return matches, deliveries

matches, deliveries = load_data()

# ---------- Load Model ----------
@st.cache_resource
def load_model():
    return pickle.load(open("live_model.pkl","rb"))

model = load_model()

# ---------- Sidebar ----------
st.sidebar.title("IPL Analytics")
page = st.sidebar.radio("Navigation",
                        ["Home","Visualizations","Live Score Predictor"])

# ---------- HOME ----------
if page == "Home":

    # Load logo
    logo = Image.open("ipl_logo.png")

    # Top Section
    col1, col2 = st.columns([1,3])

    with col1:
        st.image(logo, width=180)

    with col2:
        st.title("Indian Premier League Analytics Dashboard")
        st.write("An End-to-End Data Science Project using Python, Machine Learning and Streamlit")

    st.divider()

    # KPI Section
    st.subheader("📊 Tournament Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Matches", matches.shape[0])
    col2.metric("Total Teams", matches['team1'].nunique())
    col3.metric("Host Cities", matches['city'].nunique())
    col4.metric("Seasons Played", matches['season'].nunique())

    st.divider()

    # About Project Section
    st.subheader("📘 About the Project")

    st.write("""
    This project analyzes historical IPL cricket data to discover insights about team performance,
    player statistics and match trends. Various data visualization techniques are used to understand
    patterns in matches across different seasons.

    A machine learning regression model is developed to predict the final first-innings score
    during a live match using match progress information such as runs, overs and wickets.

    The project demonstrates a complete data science workflow including:
    - Data Cleaning & Preprocessing
    - Exploratory Data Analysis (EDA)
    - Data Visualization
    - Machine Learning Model Building
    - Deployment using Streamlit
    """)

    st.divider()

    # Instructions
    st.subheader("🧭 How to Use This Dashboard")

    st.write("""
    • Go to **Visualizations** to explore IPL statistics  
    • Go to **Live Score Predictor** to predict match scores in real-time  
    • Enter match details and click Predict Score
    """)

    st.success("Developed by Utkarsh Tiwari — BCA Final Year Project")

# ---------- VISUALIZATIONS ----------
elif page == "Visualizations":

    st.title("📊 Complete IPL Data Analysis")

    chart = st.selectbox(
        "Select Analysis",
        [
            "Top 10 Successful Teams",
            "Toss Impact on Match Result",
            "Season Wise Winners",
            "Top 10 Run Scorers",
            "Matches Hosted by Cities",
            "Correlation Heatmap",
            "Total Matches Played by Each Team",
            "Economy Rate of Bowlers",
            "Runs vs Strike Rate",
            "Match Score Distribution (Box Plot)",
            "Runs Trend Over Seasons (Line Plot)",
            "Score Frequency Histogram"
        ]
    )

    # 1
    if chart == "Top 10 Successful Teams":
        st.subheader("Top 10 Successful IPL Teams")
        fig, ax = plt.subplots()
        matches['winner'].value_counts().head(10).plot(kind='bar', ax=ax, color='orange')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 2
    elif chart == "Toss Impact on Match Result":
        st.subheader("Toss Impact on Match Result")
        toss_win = matches[matches['toss_winner'] == matches['winner']]
        fig, ax = plt.subplots()
        toss_win['toss_decision'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

    # 3
    elif chart == "Season Wise Winners":
        st.subheader("Season Wise IPL Winners")
        season_winners = matches.groupby('season')['winner'].first()
        fig, ax = plt.subplots()
        season_winners.value_counts().plot(kind='bar', ax=ax, color='green')
        st.pyplot(fig)

    # 4
    elif chart == "Top 10 Run Scorers":
        st.subheader("Top 10 Run Scorers")
        top_runs = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots()
        top_runs.plot(kind='bar', ax=ax, color='red')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 5
    elif chart == "Matches Hosted by Cities":
        st.subheader("Matches Hosted by Cities")
        fig, ax = plt.subplots()
        matches['city'].value_counts().head(10).plot(kind='bar', ax=ax, color='purple')
        st.pyplot(fig)

    # 6
    elif chart == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")
        numeric_cols = matches.select_dtypes(include=['int64','float64'])
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # 7
    elif chart == "Total Matches Played by Each Team":
        st.subheader("Matches Played by Teams")
        team_matches = pd.concat([matches['team1'], matches['team2']]).value_counts()
        fig, ax = plt.subplots()
        team_matches.head(10).plot(kind='bar', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 8
    elif chart == "Economy Rate of Bowlers":
        st.subheader("Best Economy Bowlers")
        bowler_runs = deliveries.groupby('bowler')['total_runs'].sum()
        bowler_balls = deliveries.groupby('bowler')['ball'].count()
        economy = (bowler_runs / bowler_balls) * 6
        best_economy = economy.sort_values().head(10)
        fig, ax = plt.subplots()
        best_economy.plot(kind='bar', ax=ax, color='cyan')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 9
    elif chart == "Runs vs Strike Rate":
        st.subheader("Runs vs Strike Rate")
        batsman_runs = deliveries.groupby('batter')['batsman_runs'].sum()
        balls = deliveries.groupby('batter')['ball'].count()
        strike_rate = (batsman_runs / balls) * 100
        fig, ax = plt.subplots()
        ax.scatter(batsman_runs, strike_rate)
        ax.set_xlabel("Runs")
        ax.set_ylabel("Strike Rate")
        st.pyplot(fig)

    # 10
    elif chart == "Match Score Distribution (Box Plot)":
        st.subheader("Match Score Distribution")
        total_scores = deliveries.groupby('match_id')['total_runs'].sum()
        fig, ax = plt.subplots()
        sns.boxplot(x=total_scores, ax=ax)
        st.pyplot(fig)

    # 11
    elif chart == "Runs Trend Over Seasons (Line Plot)":
        st.subheader("Runs Trend Over Seasons")
        season_runs = deliveries.merge(matches[['id','season']], left_on='match_id', right_on='id')
        season_trend = season_runs.groupby('season')['total_runs'].sum()
        fig, ax = plt.subplots()
        season_trend.plot(kind='line', marker='o', ax=ax)
        st.pyplot(fig)

    # 12
    elif chart == "Score Frequency Histogram":
        st.subheader("Score Frequency Histogram")
        total_scores = deliveries.groupby('match_id')['total_runs'].sum()
        fig, ax = plt.subplots()
        sns.histplot(total_scores, bins=20, ax=ax)
        st.pyplot(fig) 

# ---------- PREDICTOR ----------
elif page == "Live Score Predictor":

    st.title("🎯 Live Score Prediction")

    overs = st.slider("Overs Completed",1,20)
    runs = st.number_input("Current Runs",0)
    wickets = st.slider("Wickets Lost",0,10)
    runs_last_5 = st.number_input("Runs in Last 5 Overs",0)
    wickets_last_5 = st.slider("Wickets in Last 5 Overs",0,10)

    if overs>0:
        st.info(f"Current Run Rate: {runs/overs:.2f}")

    if st.button("Predict Score"):

        input_data = np.array([[overs,runs,wickets,runs_last_5,wickets_last_5]])
        prediction = model.predict(input_data)

        st.success(f"Predicted Final Score: {int(prediction[0])} Runs")
        st.balloons() 
