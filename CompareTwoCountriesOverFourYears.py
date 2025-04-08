import csv
import pandas as pd
import matplotlib.pyplot as plt

def fourCountriesCompareTwo():
    data = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="latin1")

    #These are the User inputs which will be used further down the program in order to help grab the data with data loc
    userInput = input("What country do you want?\n")
    userInputTwo = input('what is the second country?\n')
    print("=" * 50)
    print('When choosing years, you can select range from 1961 to 2019. Please type in this way: Y#### (case sensitive)')
    print("=" * 50)
    UserYearOne= input('What is the first year?\n')
    UserYearTwo= input('What is the second year?\n')
    UserYearThree= input('What is the third year?\n')
    UserYearFour= input('what is the fourth year?\n')

    #my filter is -- get me all data in Area column that is equal to user input, and get me the column equal to user input 
    countryOne= data.loc[data.Area == userInput, UserYearOne].iloc[0:23:2]
    countryOneYrTwo = data.loc[data.Area == userInput, UserYearTwo].iloc[0:23:2]
    countryOneYrThree = data.loc[data.Area == userInput, UserYearThree].iloc[0:23:2]
    countryOneYrFour = data.loc[data.Area == userInput, UserYearFour].iloc[0:23:2]


    months= data.loc[0:23:2, "Months"]

    countryTwo = data.loc[data.Area == userInputTwo, UserYearOne].iloc[0:23:2]
    countryTwoYrTwo = data.loc[data.Area == userInputTwo, UserYearTwo].iloc[0:23:2]
    countryTwoYrThree = data.loc[data.Area == userInputTwo, UserYearThree].iloc[0:23:2]
    countryTwoYrFour = data.loc[data.Area == userInputTwo, UserYearFour].iloc[0:23:2]


    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharey=True)

    #the next four ax will be the same and just plots a graph between the two countries using the above x and y axis
    #which is linked to the user input, and this is then linked to the subplot which plots 4 graphs
    ax1.plot(months, countryOne, 'bo--', label= userInput)
    ax1.plot(months, countryTwo, 'co--', label= userInputTwo)
    ax1.set_title(UserYearOne, fontsize= 12, color= 'crimson' )


    ax2.plot(months, countryOneYrTwo, 'bo--', label= userInput)
    ax2.plot(months, countryTwoYrTwo, 'co--', label= userInputTwo)
    ax2.set_title(UserYearTwo, fontsize= 12, color= 'crimson')

    ax3.plot(months, countryOneYrThree, 'bo--', label= userInput)
    ax3.plot(months, countryTwoYrThree, 'co--', label= userInputTwo)
    ax3.set_title(UserYearThree, fontsize= 12, color= 'crimson')

    ax4.plot(months, countryOneYrFour, 'bo--', label= userInput)
    ax4.plot(months, countryTwoYrFour, 'co--', label= userInputTwo)
    ax4.set_title(UserYearFour, fontsize= 12, color= 'crimson')

    #for ax in fig.get_axes():
        #ax.set(xlabel= 'Months of the year', ylabel='Temperature Change')

    for ax in fig.get_axes():
        ax.label_outer()

    fig.suptitle('Temp change over 4 Chosen Years', fontsize= 16, fontweight= 'bold', color= 'darkred')
    fig.supxlabel('Months', fontsize= 14, fontweight= 'bold', color= 'chocolate')
    fig.supylabel('Temperature Change',fontsize= 14, fontweight= 'bold', color ='chocolate')
    plt.tight_layout()
    plt.legend()
    plt.show()
