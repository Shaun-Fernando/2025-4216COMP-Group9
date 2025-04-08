import temperaturedeviation
def interface():
    print("=" * 80)
    print("|"+ " "*78 + "|")
    print("|"+ " "*26 + "Temperature Change Dataset" + " "*26 + "|")
    print("|"+ " "*78 + "|")
    print("=" * 80)
    choice=str(input("\n\nWhich program would you like to access? \n<1>Temperature Peaks \n<2> \n<3> \n<4> \n<5> \n"))
    if choice=="1":
        temperaturedeviation.tmpdev()
    elif choice=="2":
        print("Program 2")
    elif choice=="3":
        print("Program 3")
    elif choice=="4":
        print("Program 4")
    elif choice=="5":
        print("Program 5")
    else: #in case the user inputs the wrong value
        print("Incorrect Value, restarting: \n")
interface()