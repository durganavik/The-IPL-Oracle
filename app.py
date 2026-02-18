import streamlit as st
import pickle
import pandas as pd

# --- Page Setup (Tab ka naam aur icon) ---
st.set_page_config(page_title="IPL Oracle 2.0", page_icon="🏏", layout="centered")

# --- DESIGN & CSS (Sajaavat) ---
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/1088620.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         /* Glassmorphism Effect for Containers */
         div[data-testid="stExpander"] {{
             background-color: rgba(0, 0, 0, 0.7);
             border-radius: 10px;
             padding: 10px;
         }}
         /* Input Fields Text Color */
         .stNumberInput, .stSelectbox {{
             color: white;
         }}
         /* Buttons Style */
         .stButton>button {{
             background-color: #FF4B4B;
             color: white;
             font-weight: bold;
             border-radius: 10px;
             border: 2px solid #FF4B4B;
             transition: 0.3s;
         }}
         .stButton>button:hover {{
             background-color: white;
             color: #FF4B4B;
             border: 2px solid #FF4B4B;
         }}
         /* Tabs Style */
         .stTabs [data-baseweb="tab-list"] {{
             gap: 10px;
         }}
         .stTabs [data-baseweb="tab"] {{
             height: 50px;
             white-space: pre-wrap;
             background-color: rgba(0,0,0,0.5);
             border-radius: 4px 4px 0px 0px;
             gap: 1px;
             padding-top: 10px;
             padding-bottom: 10px;
             color: white;
         }}
         .stTabs [aria-selected="true"] {{
             background-color: #FF4B4B;
             color: white;
         }}
         h1, h2, h3, p, label {{
             color: white !important;
             text-shadow: 2px 2px 4px #000000;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# --- Teams & Cities ---
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

# --- Load Models ---
try:
    pipe_score = pickle.load(open('pipe.pkl', 'rb'))
    pipe_win = pickle.load(open('pipe_win.pkl', 'rb'))
except FileNotFoundError:
    st.error("⚠️ Error: Model files not found. Please run the notebook first.")
    st.stop()

# --- Main App ---
st.title("🏏 IPL Oracle: AI Match Predictor")
st.markdown("### ⚡ Powered by Machine Learning")

# --- TABS ---
tab1, tab2 = st.tabs(["🔮 Score Predictor", "🏆 Win Probability"])

# === TAB 1: SCORE ===
with tab1:
    st.markdown('<div style="background-color: rgba(0,0,0,0.6); padding: 20px; border-radius: 10px;">', unsafe_allow_html=True)
    st.header("First Innings Score")
    
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('🏏 Batting Team', sorted(teams), key='bat1')
    with col2:
        bowling_team = st.selectbox('⚾ Bowling Team', sorted(teams), key='bowl1')

    selected_city = st.selectbox('🏟️ Host City', sorted(cities), key='city1')

    col3, col4, col5 = st.columns(3)
    with col3:
        current_score = st.number_input('Current Score', min_value=0, key='score1')
    with col4:
        overs = st.number_input('Overs Done', min_value=0.0, max_value=20.0, step=0.1, key='overs1')
    with col5:
        wickets = st.number_input('Wickets Out', min_value=0, max_value=9, key='wickets1')

    last_five = st.number_input('Runs in last 5 overs', min_value=0, key='last5')

    if st.button('🔮 Predict Score', key='btn1'):
        if overs == 0:
            st.warning("Please enter overs > 0")
        else:
            balls_left = 120 - (overs * 6)
            wickets_left = 10 - wickets
            crr = current_score / overs

            input_df = pd.DataFrame(
                {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                 'current_score': [current_score], 'balls_left': [balls_left], 
                 'wickets_left': [wickets_left], 'crr': [crr], 'last_five': [last_five]}
            )

            result = pipe_score.predict(input_df)
            st.success(f"🏏 Predicted Score: {int(result[0])} - {int(result[0])+10}")
    st.markdown('</div>', unsafe_allow_html=True)

# === TAB 2: WIN PROBABILITY ===
with tab2:
    st.markdown('<div style="background-color: rgba(0,0,0,0.6); padding: 20px; border-radius: 10px;">', unsafe_allow_html=True)
    st.header("Second Innings Win Probability")
    
    col1, col2 = st.columns(2)
    with col1:
        batting_team_2 = st.selectbox('🏏 Chasing Team', sorted(teams), key='bat2')
    with col2:
        bowling_team_2 = st.selectbox('⚾ Defending Team', sorted(teams), key='bowl2')

    selected_city_2 = st.selectbox('🏟️ Host City', sorted(cities), key='city2')
    target = st.number_input('🎯 Target Score', min_value=0, key='target')

    col3, col4, col5 = st.columns(3)
    with col3:
        score_2 = st.number_input('Current Score', min_value=0, key='score2')
    with col4:
        overs_2 = st.number_input('Overs Done', min_value=0.0, max_value=20.0, step=0.1, key='overs2')
    with col5:
        wickets_2 = st.number_input('Wickets Out', min_value=0, max_value=9, key='wickets2')

    if st.button('🏆 Predict Winner', key='btn2'):
        if overs_2 == 0:
            st.warning("Please enter overs > 0")
        else:
            runs_left = target - score_2
            balls_left = 126 - (overs_2 * 6)
            wickets = 10 - wickets_2
            crr = score_2 / overs_2
            rrr = (runs_left * 6) / balls_left

            input_df = pd.DataFrame(
                {'batting_team': [batting_team_2], 'bowling_team': [bowling_team_2], 'city': [selected_city_2],
                 'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets], 
                 'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]}
            )

            result = pipe_win.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]

            st.markdown(f"### {batting_team_2} Win Probability: {round(win*100)}%")
            st.progress(win)
            
            st.markdown(f"### {bowling_team_2} Win Probability: {round(loss*100)}%")
            st.progress(loss)
    st.markdown('</div>', unsafe_allow_html=True)