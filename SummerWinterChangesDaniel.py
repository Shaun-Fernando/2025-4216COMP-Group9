import pandas as pd
import matplotlib.pyplot as plt

# Our chosen dataset loaded in
file_path = "Environment_Temperature_change_E_All_Data_NOFLAG.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Filtering the table so only temperature change is selected and then removing the Y from the data name
df_temp = df[df["Element"] == "Temperature change"]
df_temp = df_temp.rename(columns=lambda x: x[1:] if x.startswith("Y") else x)

# Define winter and summer months as per the table
winter_months = ["December", "January", "February"]
summer_months = ["June", "July", "August"]

# Filtering the data from only the specific months
df_winter = df_temp[df_temp["Months"].isin(winter_months)]
df_summer = df_temp[df_temp["Months"].isin(summer_months)]

# Extracting the year columns
years = [col for col in df_temp.columns if col.isdigit()]

# Gaining the average temperature per year for the months
winter_avg = df_winter[years].mean()
summer_avg = df_summer[years].mean()

# Converting years to integers
years_int = list(map(int, years))

# Altering the settings of the bars on the chart so it becomes a group bar chart
bar_width = 0.4
years_list = list(range(len(years_int)))
years_list_winter = [x - bar_width / 2 for x in years_list]
years_list_summer = [x + bar_width / 2 for x in years_list]

# Plotting the table and customising the colours and settings of the bars for the table
plt.figure(figsize=(14, 6))
plt.bar(years_list_winter, winter_avg, width=bar_width, label='Winter (Dec-Jan-Feb)', color='skyblue')
plt.bar(years_list_summer, summer_avg, width=bar_width, label='Summer (Jun-Jul-Aug)', color='salmon')
plt.xlabel('Year')
plt.ylabel('Average Temperature Change (°C)')
plt.title('Winter vs Summer Temperature Change Over Time (1961–2019)')
plt.xticks(years_list, years_int, rotation=45, fontsize=7)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
