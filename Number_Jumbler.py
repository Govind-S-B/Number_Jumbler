import random


def shuffle(deck):
    deck2 = []
    while len(deck) > 0:
        num = random.randint(0, len(deck)-1)
        card = deck[num]
        deck2.append(card)
        deck.remove(card)

    return deck2


strikes = 1
while True:
    win = False
    moves = 0
    op_list = shuffle(["+", "-", "/", "*"])
    num_list = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])
    dic_num = {
        "1": num_list[0],
        "2": num_list[1],
        "3": num_list[2],
        "4": num_list[3],
        "5": num_list[4],
        "6": num_list[5],
        "7": num_list[6],
        "8": num_list[7],
        "9": num_list[8],
    }
    dic_op = {
        "+": op_list[0],
        "-": op_list[1],
        "/": op_list[2],
        "*": op_list[3]
    }
    with open("./intro.txt") as f:
        print(f.read())
    while not win and strikes < 3:
        op = input("Enter Operation: ").lower()
    #   guessing
        try:
            op = dic_op[op]
            num1 = dic_num[input("Enter first number")]
            num2 = dic_num[input("Enter second number")]
            if num1 == num2:
                print("both numbers cannot be the same")
                continue

            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(abs(num1 - num2))
            elif op == "/":
                print(num1 // num2)
            elif op == "*":
                print(num1*num2)
            else:
                print("ERROR")
            moves += 1
        except KeyError:
            if op == "guess":
                win = True
                for (key) in dic_num.keys():
                    guess = input("What value does " + str(key) + " have?: ")

                    print("correct: " + str(dic_num[key]))
                    if guess == str(dic_num[key]):
                        pass
                    else:
                        win = False
                for key in dic_op.keys():
                    guess = input("What value does " + str(key) + " have?: ")
                    print("correct: " + str(dic_op[key]))
                    if guess == str(dic_op[key]):
                        pass
                    else:
                        win = False
                if win:
                    print("HURRAY YOU WON! all in  only " + str(moves) + " moves")
                else:
                    print("one or more of those was wrong, sorry")
                    print("strike " + str(strikes))
                    strikes += 1
            elif op == "quit":
                win = True
            else:
                print("ERROR: please select only numbers between 1-9 and/or  valid operator commands")
        except ZeroDivisionError:
            print("UNDEFINED")

    x = input("Would you like give feedback(leave a review)? [y/n]")
    if x == "y":
        feedback = input("Feedback:\n")
        Feedback_file = open("Number_Jumbler_Feedback.txt", "a")
        Feedback_file.write("\n" + feedback + "\n")
        Feedback_file.close()
    else:
        pass
    if strikes > 3:
        print("strike 3, you lose.")
    x = input("Would you like to play again? [y/n]")
    if x == "y":
        pass
    else:
        break
