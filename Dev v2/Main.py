def Splash():
    with open("./Splash.txt") as f:
        print(f.read())
        print()


def Menu():

    with open("./Menu.txt") as f:
        print(f.read())

    I = input("Enter option : ")

    if I == "1":
        Intro_and_Rules()  # Intro & Rules Function
    if I == "2":
        New()  # New Game Function
    if I == "3":
        Load()  # Load Game Function

    else:
        print("\nNot a valid option\n")
        Menu()


def Intro_and_Rules():
    with open("./Intro_and_Rules.txt") as f:
        print(f.read())
        print()
        Menu()


def Jmap(licht):  # Jumbled Mapper
    import random

    Jumbled = random.sample(licht, len(licht))

    Mapping = {}

    for x in range(0, len(licht)):
        Mapping[licht[x]] = Jumbled[x]

    return(Mapping)


def New():

    def Save():
        import json
        import sys

        save = {}
        save['n'] = n
        save['num'] = num
        save['op'] = op
        save['Jnum'] = Jnum
        save['Jop'] = Jop
        save['Jnum_check'] = Jnum_check
        save['Jop_check'] = Jop_check

        with open('Save.json', 'w') as outfile:
            json.dump(save, outfile)

        print("Saving and Exiting")
        sys.exit()

    n = int(input("Enter range limit : "))
    num = list(range(0, n+1))

    op = ["+", "-", "*", "/"]  # op means operation

    Jnum = Jmap(num)
    Jop = Jmap(op)

    Jnum_check = list(Jnum.values())  # Check to see remaining elements to find (Values not keys)
    Jop_check = list(Jop.values())

    def Operation():
        n1 = int(input("Enter number 1 : "))
        op = input("Enter operation : ")
        n2 = int(input("Enter number 2 : "))
        print("\nOutput is", eval(str(Jnum[n1])+str(Jop[op])+str(Jnum[n2])))
        Choose()

    def Choose():
        with open("./Choose.txt") as f:
            print(f.read())

        I = input("Enter Choice : ")

        if I == "1":
            Operation()
        if I == "2":
            Guess()
        if I == "3":
            Check()
        if I == "4":
            Save()

        else:
            print("Choose correct option ")
            Choose()

    Choose()

    def Guess():
        K = int(input("Enter Number(Jumbled) : "))
        V = int(input("Enter Guess : "))
        if V == Jnum.get(K):
            return(True)
        else:
            return(False)

    def Check():
        print(Jnum_check)
        print(Jop_check)


def Load():
    import json

    with open('Save.json') as json_file:
        save = json.load(json_file)
        n = save['n']
        num = save['num']
        op = save['op']
        Jnum = save['Jnum']
        Jop = save['Jop']
        Jnum_check = save['Jnum_check']
        Jop_check = save['Jop_check']

    print(Jnum)


Splash()
Menu()
