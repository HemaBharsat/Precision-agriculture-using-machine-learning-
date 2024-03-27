import pandas as pd
import numpy as np
import pickle

crop_recommendation_model_path = "Crop_Recommendation.pkl"
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))

input_file_path = "Data/data.csv"
output_file_path = "Data/data_p.csv"
df = pd.read_csv(input_file_path)

# Extract input features from CSV columns
N = df['N'].astype(int)
P = df['P'].astype(int)
K = df['K'].astype(int)
ph = df['ph'].astype(float)
rainfall = df['rainfall'].astype(float)
temperature = df['temperature'].astype(float)
humidity = df['humidity'].astype(float)

# Make predictions
data = np.array([N, P, K, temperature, humidity, ph, rainfall]).T
my_prediction = crop_recommendation_model.predict(data)
df['crop_prediction'] = my_prediction

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)
print("predictions saved to: " + output_file_path + "\n")

