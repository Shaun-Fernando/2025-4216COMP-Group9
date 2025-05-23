import TemperatureChangeCompareDaniel
import temperaturedeviation
import TemperaturePerYear
import CompareTwoCountriesOverFourYears
import Tempanomolyscomparedtoaverage
import longtermaverage
def interface():
    print("=" * 80)
    print("|"+ " "*78 + "|")
    print("|"+ " "*26 + "Temperature Change Dataset" + " "*26 + "|")
    print("|"+ " "*78 + "|")
    print("=" * 80)
    choice=str(input("\n\nWhich program would you like to access? \n<1>Temperature Peaks \n<2>Temperature Comparisons \n<3>Four Year Comparison \n<4>Temperature Per Year \n<5>Cumulative Temperature change for Continents \n<6>Basic Area Comparing\n<7>temperature anomolies\n<8>longterm averages"))
    if choice=="1":
        temperaturedeviation.tempdev()
    elif choice=="2":
        TemperatureChangeCompareDaniel.tempcompare()
    elif choice=="3":
        CompareTwoCountriesOverFourYears.fourCountriesCompareTwo()
    elif choice=="4":
        TemperaturePerYear.tempperyear()
    elif choice=="5":
        cumulativeContinents.cumulativeContinents()
    elif choice=="6":
        search.searchCompare()
    elif choice=="7":
        Tempanomolyscomparedtoaverage.temp_anomalies_lowest()
    elif choice=="8":
        longtermaverage.avg_temp_by_year()
    
    else: #in case the user inputs the wrong value
        print("Incorrect Value, restarting: \n")#
        interface()
interface()
