import pandas as pd
import matplotlib.pyplot as plt

def tempdev():
    country = input("What country would you like to look at? ") #user input
    country = country.upper()
    temp = float(input("What is the temperature change value you would like? ")) 
    val = input("Are you looking for temperatures above or below this value? \n 1 = above \n 2 = below\n")#asks the user if they want to see temperature above or below the value

    df = pd.read_csv("FAOSTAT_data_1-10-2022.csv")


    df = df[df['Area'].str.upper() == country]#Filter by country

    if val == "1": #if val=1, the graph shows values superior to what the user provided
        filtered_df = df[df['Value'] > temp]
        sup="superior to"
    elif val == "2":
        filtered_df = df[df['Value'] < temp] #if val=2, the graph shows values inferior to what the user provided
        sup="inferior to"
    else:
        print("Invalid choice")



    filtered_years = filtered_df['Year']#Get filtered entries per year
    filtered_year_counts = filtered_years.value_counts().sort_index()

    # Generate years and matching values
    all_years = filtered_year_counts.index.tolist() #list for the years in which the temperature change matches the requirement
    filtered_vals = filtered_year_counts.tolist() #list of the amount of times this happens in the year



    x = list(range(len(all_years)))
    bar_width = 0.5


    plt.figure(figsize=(12, 6))
    plt.bar(x, filtered_vals, width=bar_width)

    plt.title(f'{country.title()} Temperature Data by Year\nTemperature Difference {sup} {temp}°C')
    plt.ylabel('Number of Entries Matching Condition')
    plt.xticks(x, all_years, rotation=45)
    plt.show()
