import pandas as pd

# Check Deliveries File
dels = pd.read_csv('deliveries.csv')
print("Deliveries Data Shape:", dels.shape)
