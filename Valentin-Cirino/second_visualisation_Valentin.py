import matplotlib.pyplot as plt
import csv
with open('FAOSTAT_data_1-10-2022.csv', 'r') as f:
    csv_reader= csv.reader(f)
    bel=[]
    spa=[]
    years=[]
    for i in range(2001,2020,2):
        years.append(i)
    for i in f:
        b=next(csv_reader)
        if b[3]=="Russian Federation" and b[7]=="January" and int(b[8]) in years:
            bel.append(float(b[11]))
        if b[3]=="Luxembourg" and b[7]=="January" and int(b[8]) in years:
            spa.append(float(b[11]))
x_values = list(range(len(bel)))

plt.figure(figsize=(10, 5))
plt.plot(years,bel,"mD:",label="Russia")
plt.plot(years,spa,"mD:",color="r",label="Luxembourg")
plt.xticks(years)
plt.xlabel("Years")
plt.ylabel("Temperature Change")
plt.title("Temperature Change in January from 2001 to 2019")
plt.legend()
plt.show()