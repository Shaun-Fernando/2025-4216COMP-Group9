import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

df = pd.read_csv(r"C:\Users\shaun\OneDrive\Documents\Computer Science\2025-4216COMP-Group9\Environment_Temperature_change_E_All_Data_NOFLAG.csv")  

fig, ax = plt.subplots()  
xInput = np.empty(59)  
yInput = np.empty(59)  

ax.set_title("Cumulative Temperature Change in August for Continents")  
ax.set_xlabel("Year")  
ax.set_ylabel("Temperature change")  

for i in range(1, 9300):  

    if df["Area"][i] == "Europe" or df["Area"][i] == "Asia" or df["Area"][i] == "Northern America" or df["Area"][i] == "South America" or df["Area"][i] == "Oceania" or df["Area"][i] == "Africa":  

        if df["Months"][i] == "August":  

            if df["Element"][i] == "Temperature change":

                for j in range (59):  

                    xInput[j] = j + 1961 

                    yInput[j] = df.iloc[i][j+7] + yInput[j-1]


                ax.plot(xInput, yInput, label = df["Area"][i])  

                ax.legend() 

                for k in range (59):  
                    yInput[k] = 0
plt.show()
