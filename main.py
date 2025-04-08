def interface():
    print("=" * 80)
    print("|"+ " "*78 + "|")
    print("|"+ " "*26 + "Temperature Change Dataset" + " "*26 + "|")
    print("|"+ " "*78 + "|")
    print("=" * 80)
    choice=str(input("\n\nWhich program would you like to access? \n<1> "))
    if choice=="1":
        #program 1
    elif choice=="2":
        #program 2
    elif choice=="3":
        #program 3
    elif choice=="4":
        #program 4
    elif choice=="5":
        #program 5
    elif choice=="6":
        #program 6
    else:
        print("Incorrect Value, restarting: \n")
        interface()

interface()