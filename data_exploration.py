import pandas as pd
import numpy as np
import os 

file_path = "C:\\Users\\Hema\\PycharmProjects\\model_files\\Data\\crop_recommendation.csv"
training_data = pd.read_csv(file_path)

n_range = (training_data['N'].min(), training_data['N'].max())
p_range = (training_data['P'].min(), training_data['P'].max())
k_range = (training_data['K'].min(), training_data['K'].max())
temp_range = (training_data['temperature'].min(), training_data['temperature'].max())
humidity_range = (training_data['humidity'].min(), training_data['humidity'].max())
ph_range = (training_data['ph'].min(), training_data['ph'].max())
rainfall_range = (training_data['rainfall'].min(), training_data['rainfall'].max())

print("N range: ", n_range)
print("P range: ", p_range)
print("K range: ", k_range)
print("Temperature range: ", temp_range)
print("Humidity range: ", humidity_range)
print("pH range: ", ph_range)
print("Rainfall range: ", rainfall_range)
