import seaborn as sns
import pandas as pd
import numpy as np
from weather_data import london_data

# Look at the first few rows of the dataset
print(london_data.head())

# Look at rows 100-199
print(london_data.iloc[100:200])

# Take a look at how many datapoints there are
print(len(london_data))

# Save the 'TemperatureC' column to a variable
temp = london_data['TemperatureC']

# Find the average temperature in London in 2015
average_temp = np.mean(temp)

# Calculate the variance of the temperature column
temperature_var = np.var(temp)
print(temperature_var)

# Calculate the standard deviation of the tempeature column
temperature_standard_deviation = np.std(temp)
#print(temperature_standard_deviation)

# Filter the temperature by the months June and July
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

# Calculate the mean temperature in London for June and July
print(np.mean(june))
print(np.mean(july))

# Calculate the standard deviation of temperature in London for June and July
print(np.std(june))
print(np.std(july))

# Calculate the mean and standard deviation for temperature for the rest of the months
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# Calculate the mean and standard deviation for rainfall for the rest of the months
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["dailyrainMM"]
  print("The mean rainfall in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of rainfall in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# Calculate the mean and standard deviation for rainfall based on the time of day
for i in range(0, 24):
  hour = london_data.loc[london_data["hour"] == i]["dailyrainMM"]
  print("The mean rainfall in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation of rainfall in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")
