### **📅 Daily Progress Report: Day 2**
==(DT:11-JAN-26)== 

**Topic:** Player Performance Analysis (Univariate Analysis)

#### **1. Key Activities Completed:**

- **Loaded Ball-by-Ball Data:** Successfully integrated the deliveries.csv dataset (approx. 2.6 Lakh records) to perform granular analysis.
    
- **Batsman Analysis (Orange Cap Logic):**
    
    - Grouped data by players to calculate total runs scored in IPL history.
        
    - **Result:** Identified **Virat Kohli** as the all-time leading run-scorer.
        
- **Bowler Analysis (Purple Cap Logic):**
    
    - Applied **Data Filtering** to exclude non-bowler dismissals (like 'run out').
        
    - Calculated total wickets taken by each bowler.
        
    - **Result:** Identified **Yuzvendra Chahal** as the all-time leading wicket-taker.
        

#### **2. Visualizations Created:**

- **Bar Chart 1:** Top 10 Run Scorers (Visualized using a summer color palette).
    
- **Bar Chart 2:** Top 10 Wicket Takers (Visualized using a magma color palette).
    

#### **3. Technical Concepts Applied:**

- **Pandas Functions:** groupby(), sum(), sort_values(), .isin() (for filtering specific dismissal types).
    
- **Visualization:** Advanced bar plotting with Seaborn.