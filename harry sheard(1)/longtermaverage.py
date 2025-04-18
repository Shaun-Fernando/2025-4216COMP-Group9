import pandas as pd
import matplotlib.pyplot as plt

def avg_temp_by_year():
    # Load data
    df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG (1).csv", encoding='ISO-8859-1')

    # Filter only temperature change rows
    df_temp = df[df['Element'] == 'Temperature change']

    # Get list of unique countries
    countries = sorted(df_temp['Area'].unique())

    # Display countries
    print("Available countries:")
    for i, country in enumerate(countries):
        print(f"{i + 1}. {country}")

    # User selects a country
    choice = int(input("\nEnter the number of the country you want to select: ")) - 1
    selected_country = countries[choice]

    # Filter for selected country
    country_data = df_temp[df_temp['Area'] == selected_country]

    # Average over months for each year
    years = [col for col in df_temp.columns if col.startswith('Y')]
    avg_by_year = country_data[years].mean()

    # Plotting
    plt.figure(figsize=(12, 6))
    avg_by_year.plot()
    plt.title(f"Long-term Average Temperature Change in {selected_country}")
    plt.xlabel("Year")
    plt.ylabel("Temperature Change (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Optional standalone run
if __name__ == "__main__":
    avg_temp_by_year()
