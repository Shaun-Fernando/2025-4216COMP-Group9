import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("M:\csws\matplot\Environment_Temperature_change_E_All_Data_NOFLAG.csv",encoding='latin1')

df_temp_change = df[df["Element"] == "Temperature change"].drop(columns=["Area Code", "Months Code", "Element Code", "Element", "Unit"])
df_temp_change = df_temp_change.rename(columns=lambda x: x[1:] if x.startswith("Y") else x)
years = [str(year) for year in range(1961,2020)]
print("This algorithm requires you to enter 5 countries")
country1 = input("Enter a country")
country2 = input("Enter a country")
country3 = input("Enter a country")
country4 = input("Enter a country")
country5 = input("Enter a country")
totals = [str(total) for total in range(0,5)]
total = 0
total_set = 0
countries = (country1,country2,country3,country4,country5)
for i in range(0,5):
    country = countries[i]
    df_country = df_temp_change[df_temp_change["Area"] == country][years].mean().values.flatten()
    if df_country.size == 0:
        print("Error no data available for country entered")
        break
    else:
        for x in range(0,58):
            value = df_country[x]
            total = total + value
    totals_set =+ 1
    totals[total_set] = str.total
fig, (left,right) = plt.subplots(1,2)

left.set_title("Bar Plot")
left.set_title("Scatter Plot")

left.bar(countries, totals)
right.scatter(countries, totals)

plt.show()