import random

b = random.randint(1, 3)
c = ()

while True:
    a = input()
    if a == "!exit":
        print("Bye!")
        break
    if a != "rock" and a != "paper" and a != "scissors":
        print("Invalid input")
    elif b == 1:
        c = "rock"
        if a == "rock":
            print("There is a draw (" + c +")")
        elif a == "paper":
            print("Well done. Computer chose " + c + " and failed")
        else:
            print("Sorry, but computer chose " + c)
    elif b == 2:
        c = "paper"
        if a == "paper":
            print("There is a draw (" + c +")")
        elif a == "scissors":
            print("Well done. Computer chose " + c + " and failed")
        else:
            print("Sorry, but computer chose " + c)
    elif b == 3:
        c = "scissors"
        if a == "scissors":
            print("There is a draw (" + c +")")
        elif a == "rock":
            print("Well done. Computer chose " + c + " and failed")
        else:
            print("Sorry, but computer chose " + c)
