''''
it is reccomended that you read this program from bottom to top
'''
import sys
# for exiting the program
import json
# for loading and storing save files
import random
# used in jmap
import re

expr = guess_count = n = num = op = Jnum = Jop = Jnum_check = Jop_check = 1  # Initialising Global Variables


def Jmap(licht):  # Jumbled Mapper.

    Jumbled_licht = random.sample(licht, len(licht))  # comletely randomizes the list

    Mapping = {}

    for i in range(0, len(licht)):
        Mapping[licht[i]] = Jumbled_licht[i]

    return Mapping

# main game function, just call game() to run the game


def Game(x):  # x is true if its a new game, false if its been loaded

    # need global keyword so it uses the previously initialised global variables and doesnt create new local variables
    global guess_count  # counts how many consecutive chances the player has left to guess
    global n  # sets size of jumble, numbers from 0 to n are jumbled in the game
    global num  # list of all the numbers to be jumbled
    global op  # list of all valid operations
    global Jnum  # a dictionary that maps the jumbled numbers
    global Jop  # dictionary that maps the jumbled operations
    global Jnum_check  # list of all numbers player has left to correctly guess
    global Jop_check  # list of all operations player has left to correctly guess

    if x is True:  # for new game

        n = int(input("Enter range limit : "))
        num = list(range(0, n + 1))

        op = ["+", "-", "*", "/"]

        # initializes the dictionaries
        Jnum = Jmap(num)
        Jop = Jmap(op)

        Jnum_check = list(Jnum.keys())
        Jop_check = list(Jop.keys())

        guess_count = 3  # setting up for the initial guess

    if x is False:  # for loaded game

        with open('Save.json') as json_file:
            # save is the dictionary with all the saved data
            save = json.load(json_file)
            n = save['n']
            num = save['num']
            op = save['op']
            Jnum = save['Jnum']
            Jop = save['Jop']
            Jnum_check = save['Jnum_check']
            Jop_check = save['Jop_check']
            guess_count = save['guess_count']

        k = list(Jnum.keys())
        v = list(Jnum.values())
        Jnum.clear()

        for i in range(0, len(k)):
            k[i] = int(k[i])

        for i in range(0, len(k)):
            Jnum.update({k[i]: v[i]})

    def Save():

        global guess_count  # counts how many consecutive chances the player has left to guess
        global n  # sets size of jumble, numbers from 0 to n are jumbled in the game
        global num  # list of all the numbers to be jumbled
        global op  # list of all valid operations
        global Jnum  # a dictionary that maps the jumbled numbers
        global Jop  # dictionary that maps the jumbled operations
        global Jnum_check  # list of all numbers player has left to correctly guess
        global Jop_check  # list of all operations player has left to correctly guess

        save = {}
        save['n'] = n
        save['num'] = num
        save['op'] = op
        save['Jnum'] = Jnum
        save['Jop'] = Jop
        save['Jnum_check'] = Jnum_check
        save['Jop_check'] = Jop_check
        save['guess_count'] = guess_count

        with open('Save.json', 'w') as outfile:
            json.dump(save, outfile)

        print("Saving and Exiting")
        sys.exit()

    def Check():

        global Jnum_check
        global Jop_check

        print("The numbers left to find out are", Jnum_check)
        print("The operations left to find out are", Jop_check)

        Choose()

    def Guess():

        global guess_count
        global Jnum
        global Jop
        global Jnum_check
        global Jop_check
        global expr

        K = expr[0]  # K is the symbol # key
        V = expr[2]  # V is the value that symbol holds # value

        # x only gives true for correctly guessed operations; x is the key-value check for operations
        if K in Jop.keys():
            x = (V == Jop[K])  # we need x as a dummy variable in case Jop[K] gives KeyError.
        else:
            x = False

        # y is true if player correctly guesses jumbled number; y is the key-value check for number
        y = (V == str(Jnum[int(K)]))

        if x or y:
            print("Your Guess was right !")
            guess_count = 3  # resets chances for guessing

            # removes the correctly guessed number or operations from checklists(Jnum_check and Jop_check)
            if K in list(map(str, Jnum_check)):
                Jnum_check.remove(int(K))
            elif K in Jop_check:
                Jop_check.remove(K)
            else:
                pass

            if len(Jop_check) == len(Jnum_check) == 0:  # if there is nothing left to guess
                print("You Won !")
                sys.exit()

        else:
            print("Guess Wrong")
            guess_count -= 1
            print("You have", guess_count, "consecutive chances left")
            if guess_count == 0:
                print("You Lose")
                sys.exit()

        Choose()

    def Operation():
        global expr

        try:

            n1 = int(expr[0])
            op = expr[1]
            n2 = int(expr[2])
            print("Output is", eval(str(Jnum[n1]) + str(Jop[op]) + str(Jnum[n2])))
            Choose()
        except:
            print("Something Funny Happened ! Please try again ")
            Operation()

    def Choose():

        global expr

        with open("./Choose.txt") as f:
            print(f.read())

        INPUT = input("CMD : ")
        cmd = INPUT.split()[0]
        try:
            expr = re.split(r'(\D)', INPUT.split()[1])

        except:
            pass

        if cmd == "oper":

            Operation()
        if cmd == "guess":

            Guess()
        if cmd == "check":

            Check()
        if cmd == "save":

            Save()

        else:
            print("Not a valid option")
            Choose()

    Choose()


def Intro_and_Rules():
    with open("./Intro_and_Rules.txt") as f:
        print(f.read())
        Menu()


def Menu():

    with open("./Menu.txt") as f:
        print(f.read())

    INPUT = input("Enter option : ")

    if INPUT == "1":
        Intro_and_Rules()
    if INPUT == "2":
        Game(True)  # New
    if INPUT == "3":
        Game(False)  # Load

    else:
        print("Not a valid option")
        Menu()


def Splash():                           # This is the banner text
    with open("./Splash.txt") as f:
        print(f.read())


Splash()
Menu()
