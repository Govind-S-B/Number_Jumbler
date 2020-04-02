def Menu():

    with open("./Menu.txt") as f:
        print(f.read())

    I = int(input("Enter the number coresponding to the option : "))

    if I == 2:
        LoadGame()
    if I == 3:
        NewGame()
    if I == 4:
        Intro_and_Rules()

    else:
        print("No option has been selected")
        Menu()


Menu()
