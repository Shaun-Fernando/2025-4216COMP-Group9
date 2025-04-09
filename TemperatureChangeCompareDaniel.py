import matplotlib.pyplot as plt
import pandas as pd

def tempcompare():
   # Our chosen dataset loaded in
   file_path = "Environment_Temperature_change_E_All_Data_NOFLAG.csv"
   df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Extracting the temperature data and removing the Y so it can become an int
   df_temp = df[df["Element"] == "Temperature change"].drop(columns=["Area Code", "Months Code", "Element Code", "Element", "Unit"])
   df_temp = df_temp.rename(columns=lambda x: x[1:] if x.startswith("Y") else x) 

# Listing countries
   valid_countries = df_temp["Area"].unique()

   def plot_temperature_change(country1, country2):
       years = [str(year) for year in range(1961, 2020)]
    
       if country1 not in valid_countries:
           print(f"Error: {country1} not found in dataset. Please check spelling and try again.")
           return
       if country2 not in valid_countries:
           print(f"Error: {country2} not found in dataset. Please check spelling and try again.")
           return
    
    # Filtering data from the table for the selected countries
       data1 = df_temp[df_temp["Area"] == country1][years].mean().values.flatten()
       data2 = df_temp[df_temp["Area"] == country2][years].mean().values.flatten()
    
       if data1.size == 0 or data2.size == 0:
        print("Error: One or both selected countries have no data available.")
        return
    
    # Converting years to integers for plotting
       year_values = list(range(1961, 2020))
    
    # Plotting the data
       fig, ax = plt.subplots()
       ax.plot(year_values, data1, 'mD:', label=country1)
       ax.plot(year_values, data2, 'ro--', label=country2)
    
       plt.xlabel("Year")
       plt.ylabel("Temperature Change (°C)")
       plt.title(f"Temperature Change in {country1} and {country2} (1961-2019)")
       plt.xticks(year_values, rotation=45, fontsize=8)
       plt.legend()
       plt.grid(True)
       plt.show()

# Get the user's input for the chosen countries
   print("Available countries:")
   print(", ".join(valid_countries[:10]) + "...")  # Showing a small preview of countries for the user
   country1 = input("Enter the first country  (With capitalisation): ")
   country2 = input("Enter the second country (With capitalisation): ")

   plot_temperature_change(country1, country2)


