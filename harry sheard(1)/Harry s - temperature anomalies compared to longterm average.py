import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with correct encoding and built-in file path
def load_data():
    file_path = "Environment_Temperature_change_E_All_Data_NOFLAG (1).csv"
    return pd.read_csv(file_path, encoding='ISO-8859-1')

# Get list of unique countries
def get_countries(df):
    return sorted(df['Area'].unique())

# Get the lowest temperature anomaly for each year for a specific country
def get_lowest_yearly_temps(df, country):
    # Filter data for the selected country and only for 'Temperature change' element
    country_data = df[(df['Area'] == country) & (df['Element'] == 'Temperature change')]

    # Years of interest
    years = [col for col in df.columns if col.startswith('Y')]

    # Get the minimum value per year
    lowest_yearly_temps = []
    for year in years:
        year_values = country_data[year].dropna()
        if not year_values.empty:
            lowest_yearly_temps.append((year[1:], year_values.min()))

    return lowest_yearly_temps

# Plot the graph
def plot_temperature_trend(temp_data, country):
    years, temps = zip(*temp_data)
    years = list(map(int, years))
    
    plt.figure(figsize=(12, 6))
    plt.plot(years, temps, marker='o', linestyle='-', color='blue')
    plt.title(f"Lowest Recorded Temperature Anomalies per Year in {country}")
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main app logic
def main():
    df = load_data()

    countries = get_countries(df)
    print("Available countries:")
    for i, country in enumerate(countries):
        print(f"{i + 1}. {country}")

    choice = int(input("\nSelect a country by number: "))
    selected_country = countries[choice - 1]

    temp_data = get_lowest_yearly_temps(df, selected_country)
    plot_temperature_trend(temp_data, selected_country)

if __name__ == "__main__":
    main()
