import random

c = ()

#test
player_names = ['batas 150', 'kaloy 500', 'kitteh 95']
#test end

#player = open('rating.txt', 'r', encoding='utf-8')

user = input("Enter your name:")
test_user = ""
matches = 0
score = 0
index = 0

for name in player_names:
    test_user = name.split()
    if user == test_user[0]:
        print("Hello, " + user)
        print("Your rating: " + test_user[1])
        matches += 1
        score = int(test_user[1])
        index = player_names.index(name)
        pass

if matches == 0:
    print("Hello, " + user)
    print("Your rating: 0")
    player_names.append(user + " 0")
    index = len(player_names) - 1

print(player_names)
print(test_user)
print(index)

while True:
    a = input()
    b = random.randint(1, 3)
    if a == "!exit":
        print("Bye!")
        player_names[index] = user + " "  + str(score)
        print(player_names)
        break
    if a == "!rating":
       print(score)
    elif a != "rock" and a != "paper" and a != "scissors" and a != "!rating":
        print("Invalid input")
    elif b == 1:
        c = "rock"
        if a == "rock":
            print("There is a draw (" + c +")")
            score += 50
        elif a == "paper":
            print("Well done. Computer chose " + c + " and failed")
            score += 100
        else:
            print("Sorry, but computer chose " + c)
    elif b == 2:
        c = "paper"
        if a == "paper":
            print("There is a draw (" + c +")")
            score += 50
        elif a == "scissors":
            print("Well done. Computer chose " + c + " and failed")
            score += 100
        else:
            print("Sorry, but computer chose " + c)
    elif b == 3:
        c = "scissors"
        if a == "scissors":
            print("There is a draw (" + c +")")
            score += 50
        elif a == "rock":
            print("Well done. Computer chose " + c + " and failed")
            score += 100
        else:
            print("Sorry, but computer chose " + c)
    print("rating: " + str(score))
