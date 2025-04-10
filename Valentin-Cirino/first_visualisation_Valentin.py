import matplotlib.pyplot as plt
import csv

with open('FAOSTAT_data_1-10-2022.csv', 'r') as f:
    csv_reader = csv.reader(f)
    bel = []
    spa = []
    years = []
    
    for i in range(1990, 2021, 2):
        years.append(i)
    years.remove(2012)
    
    for i in f:
        b = next(csv_reader)
        if b[3] == "Mozambique" and b[7] == "January" and int(b[8]) in years and int(b[8]) != 2012:
            bel.append(float(b[11]))
        if b[3] == "Singapore" and b[7] == "January" and int(b[8]) in years and int(b[8]) != 2012:
            spa.append(float(b[11]))

bar_width = 0.4
x_indexes = range(len(years))

plt.figure(figsize=(12, 6))
plt.bar([x - bar_width/2 for x in x_indexes], bel, width=bar_width, label="Mozambique", color='blue')
plt.bar([x + bar_width/2 for x in x_indexes], spa, width=bar_width, label="Singapore", color='red')

plt.xticks(ticks=x_indexes, labels=years, rotation=45)
plt.xlabel("Years")
plt.ylabel("Temperature Change (°C)")
plt.title("Temperature Change in January (1990-2020)")
plt.axhline(0, color='black', linewidth=0.8)  
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
