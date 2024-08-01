import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load Models
with open('model.pkl', 'rb') as file:
  model = pickle.load(file)

def run():
  # membuat judul
  st.title('Premiere League Result Prediction')
  # buat garis
  st.markdown('---')
  with st.form('Match Form'):
    # nama tim home
    homeTeam = st.selectbox(
    "Select Home Team",
    ('Arsenal', 'Aston Villa', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton', 'Bournemouth', 'Bradford', 'Brentford', 'Brighton', 'Burnley', 'Cardiff', 'Chelsea', 'Charlton', 'Coventry', 'Crystal Palace', 'Derby', 'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Portsmouth', 'QPR', 'Reading', 'Sheffield United', 'Southampton', 'Stoke', 'Sunderland', 'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wolves'),)
    st.write("You selected:", homeTeam)
    # nama tim away
    awayTeam = st.selectbox(
    "Select Away Team",
    ('Arsenal', 'Aston Villa', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton', 'Bournemouth', 'Bradford', 'Brentford', 'Brighton', 'Burnley', 'Cardiff', 'Chelsea', 'Charlton', 'Coventry', 'Crystal Palace', 'Derby', 'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Portsmouth', 'QPR', 'Reading', 'Sheffield United', 'Southampton', 'Stoke', 'Sunderland', 'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wigan', 'Wolves'),)
    st.write("You selected:", awayTeam)
    # Full Time Home Goals
    FTHG = st.slider('Full Time Home Goals', min_value=0, max_value=20, value=0)
    # Full Time Away Goals
    FTAG = st.slider('Full Time Away Goals', min_value=0, max_value=20, value=0)
    # Half Time Home Goals
    HTHG = st.slider('Half Time Home Goals', min_value=0, max_value=20, value=0)
    # Half Time Away Goals
    HTAG = st.slider('Half Time Away Goals', min_value=0, max_value=20, value=0)
    # Half Time Result
    halfTimeR = st.selectbox(
    "Half Time Result",
    ('H','A','D'),)
    st.write("You selected:", halfTimeR)
    # Home Team Shots
    HS = st.slider('Home Team Shots', min_value=0, max_value=50, value=5)
    # Away Team Shots
    AS = st.slider('Away Team Shots', min_value=0, max_value=50, value=5)
    # Home Team Shots on target
    HST = st.slider('Home Team Shots on Target', min_value=0, max_value=30, value=5)
    # Away Team Shots on target
    AST = st.slider('Away Team Shots on Target', min_value=0, max_value=30, value=5)
    # Home Team Corners
    HC = st.slider('Home Team Corners', min_value=0, max_value=20, value=5)
    # Away Team Corners
    AC = st.slider('Away Team Corners', min_value=0, max_value=20, value=5)
    # Home Team Fouls Committed
    HF = st.slider('Home Team Fouls Committed', min_value=0, max_value=40, value=5)
    # Away Team Fouls Committed
    AF = st.slider('Away Team Fouls Committed', min_value=0, max_value=40, value=5)
    # Home Team Yellow Cards
    HY = st.slider('Home Team Yellow Cards', min_value=0, max_value=20, value=5)
    # Away Team Yellow Cards
    AY = st.slider('Away Team Yellow Cards', min_value=0, max_value=20, value=5)
    # Home Team Red Cards
    HR = st.slider('Home Team Red Cards', min_value=0, max_value=10, value=5)
    # Away Team Red Cards
    AR = st.slider('Away Team Red Cards', min_value=0, max_value=10, value=5)
    # garis
    st.markdown('---')

    # submit button
    submitted = st.form_submit_button('Predict')
  data_inf = {
    'HomeTeam': homeTeam,
    'AwayTeam': awayTeam,
    'FTHG': FTHG,
    'FTAG': FTHG,
    'HTHG': HTHG,
    'HTAG': HTAG,
    'HTR': halfTimeR,
    'HS': HS,
    'AS': AS,
    'HST': HST,
    'AST': AST,
    'HC': HC,
    'AC': AC,
    'HF': HF,
    'AF': AF,
    'HY': HY,
    'AY': AY,
    'HR': HR,
    'AR': AR,}
  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)

  if submitted:
    predictions = model.predict(data_inf)
    # buat garis
    st.markdown('---')
    st.write('### Match Result: ', str(int(predictions)))
    

    pred = model.predict_proba(data_inf)
    # Convert probabilities to betting odds
    # Avoid division by zero 
    epsilon = 1e-10
    betting_odds = 1 / (pred + epsilon)

    # Cap the maximum odds 
    max_odds = 5  
    betting_odds = np.clip(betting_odds, 0, max_odds)

    # better readability
    np.set_printoptions(suppress=True, formatter={'float_kind': '{:0.2f}'.format})

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Adding decimal variation
    odds_normalized = betting_odds + np.random.uniform(-0.50, 0.50, betting_odds.shape)
    odds_normalized = np.round(odds_normalized, 2)
    odds_normalized1 = pd.DataFrame(odds_normalized)
    st.markdown('---')
    st.write('### Odds Result: ', odds_normalized1)
    st.write('Home win Odds = 0')
    st.write('Away Win odds = 1')
    st.write('Draw Odds = 2')
  # buat garis
  st.markdown('---')









if __name__ == '__main__':
  run()