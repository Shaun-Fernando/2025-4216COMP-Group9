def interface():
    print("=" * 80)
    print("|"+ " "*78 + "|")
    print("|"+ " "*26 + "Temperature Change Dataset" + " "*26 + "|")
    print("|"+ " "*78 + "|")
    print("=" * 80)
    choice=str(input("\n\nWhich program would you like to access? \n<1> \n<2> \n<3> \n<4> \n<5> \n<6> "))
    if choice=="1":
        print("Program 1")
    
    if choice=="2":
        print("Program 2")
    if choice=="3":
        print("Program 3")
    if choice=="4":
        print("Program 4")
    if choice=="5":
        print("Program 5")
    if choice=="6":
        print("Program 6")
    else: #in case the user inputs the wrong value
        print("Incorrect Value, restarting: \n")
        interface()

interface()