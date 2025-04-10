import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

def searchCompare():
    df = pd.read_csv(r"C:\Users\shaun\OneDrive\Documents\Computer Science\2025-4216COMP-Group9\Environment_Temperature_change_E_All_Data_NOFLAG.csv")  
    
    fig, ax = plt.subplots()  
    xInput = np.empty(59)  
    yInput = np.empty(59)
    areas = []
    
    noAreas = int(input("How many areas do you want to plot? "))
    for i in range(noAreas):  
        area = input("Enter the area you want to plot (With first character capitalised): ")
        areas.append(area)
    month = input("Enter the month you want to plot (With first character capitalised): ")
    
    ax.set_title("Temperature change in " + month) 
    ax.set_xlabel("Year")  
    ax.set_ylabel("Temperature change") 
    
    for j in range(len(areas)):
        
            for k in range(1, 9300):  
                    
                if df["Area"][k] == areas[j]:
    
                    if df["Months"][k] == month:
                         
                        if df["Element"][k] == "Temperature change":  
    
                            for l in range (59):  
    
                                xInput[l] = l + 1961 
                                yInput[l] = df.iloc[k][l+7]  
    
                            ax.plot(xInput, yInput, label = df["Area"][k])  
    
                            ax.legend() 
    
    plt.show()
