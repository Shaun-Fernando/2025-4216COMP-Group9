import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="latin1")

#this is the user input for the columns
print("=" * 50)
print('When choosing a year please stick to this format: Y#### (case sensitive)')
print("=" * 50)
userInput = input("What Year do you want?\n")


#This locs the rows from the column Area that are equal to Senegal, and depending on what year the User types in
#will depend on what column is grabbed, the same is for Russia
D= data.loc[data.Area== 'Senegal', userInput].iloc[0:23:2]

#grabbing the months that i need from the database asnd giving them the same index as the Y axis data above with iloc
C= data.loc[0:23:2, "Months"]

F = data.loc[data.Area =='Russian Federation', userInput].iloc[0:23:2]

#plotting two different graphs 
fig, (ax1, ax2) = plt.subplots(2, sharey=True)

#this is just separetely outputting the two different graphs with specific graph features 
markerline, stemlines, baseline = ax1.stem(
    C, D, linefmt='grey', markerfmt='D', bottom=1.1, label= 'Senegal')
markerline.set_markerfacecolor('none')
ax1.set_title('Senegal', fontsize= 14, color= 'saddlebrown', fontweight= 'bold' )


markerline, stemlines, baseline = ax2.stem(
    C, F, linefmt='grey', markerfmt='D', bottom=1.1, label='Russia')
markerline.set_markerfacecolor('none')
ax2.set_title('Russia', fontsize= 14, color= 'saddlebrown', fontweight= 'bold' )


for ax in fig.get_axes():
    ax.label_outer()

fig.suptitle('The Hottest vs Coldest Country in the world for: {}'.format(userInput), fontsize= 16, fontweight= 'bold', color= 'forestgreen')
fig.supxlabel('Months', fontsize= 14, fontweight= 'bold', color= 'sienna')
fig.supylabel('Temperature Change',fontsize= 14, fontweight= 'bold', color ='sienna')
plt.tight_layout()
plt.show()
