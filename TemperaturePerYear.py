import matplotlib.pyplot as plt 
import pandas as pd 

def tempperyear():
#Read in the dataset from the csv file 

  df = pd.read_csv("M:\csws\matplot\Environment_Temperature_change_E_All_Data_NOFLAG.csv",encoding='latin1') 

#read in the data for temperature changes and reset column headers for years as the preset ones returned errors 

  df_temp_change = df[df["Element"] == "Temperature change"].drop(columns=["Area Code", "Months Code", "Element Code", "Element", "Unit"]) 

  df_temp_change = df_temp_change.rename(columns=lambda x: x[1:] if x.startswith("Y") else x) 

#take user input 

  country = input("Enter a country") 

#set a lis of the years the dataset covers 

  years = [str(year) for year in range(1961,2020)] 

#retrieve values for country user entered

  values = df_temp_change[df_temp_change["Area"] == country][years].mean().values.flatten() 

#return error if value user enters is not valid, if valid returns plot 

  if values.size == 0: 
     print("Error: No data is available for the country you entered") 

  else: 
   fig, ax = plt.subplots() 
   ax.plot(years, values,'mD:') 
   plt.title("Temperature Change over "+ country + " between 1961 and 2019") 
   plt.xlabel("Year", fontsize =8) 
   plt.ylabel("Temperature Change", fontsize = 8) 
   plt.xticks(fontsize=6) 
   plt.grid(True) 
   plt.show()