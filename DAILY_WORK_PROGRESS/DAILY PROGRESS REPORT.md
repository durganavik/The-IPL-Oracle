### 📅 **Daily Progress Report: Day 1 (Project Execution)**    ==(DT:10-JAN-26)== 

**1. Project Setup & Data Acquisition:**

- I finalized the **Project Title:** "The IPL Oracle: Performance Analysis & Match Predictor".
    
- I defined the **Project Scope:** Combining EDA (Analysis) with Machine Learning (Score & Win Prediction) to meet college requirements.
    
- I downloaded the **Complete Dataset** from Kaggle, which includes two essential files:
    
    - matches.csv (Match results).
        
    - deliveries.csv (Ball-by-ball data for prediction).
        
	- I successfully fixed **File Path Errors** (FileNotFoundError, PermissionError) and organized the folder structure.
    

**2. Coding & Implementation:**

- Created the main project file: **IPL_Project_Main.ipynb**.
    
- **Data Loading:** Successfully loaded both CSV files into Python using Pandas.
    
- **Data Inspection:** Checked the shape (number of rows/columns) and identified key columns like season, winner, and total_runs.
    

**3. Exploratory Data Analysis (EDA) - Started:**  
We completed **Task 1 & Task 2** of your College PDF:

- **Visualization 1 (Time Trend):** Created a Bar Chart for "Total Matches Played Per Season (2008-2024)".
    
    - Insight: Observed the fluctuation in matches due to the addition of new teams in 2011-2013.
        
- **Visualization 2 (Univariate Analysis):** Created a Horizontal Bar Chart for "Most Successful Teams".
    
    - Insight: Identified the top dominating teams (MI, CSK) based on total wins.
        

**4. Technical Skills Applied:**

- **Libraries Used:** Pandas (Data Handling), Matplotlib & Seaborn (Visualization).
    
- **Concepts:** read_csv, .shape, .value_counts(), barplot.