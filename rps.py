import random
play = ["Rock" , "Paper" , "Scissors"]
computer = random.choice(play)
player = False
while player == False:
    player=input("Rock, Paper or Scissors ? ")
    if computer == player:
        print("TIE!! You both have chosen same")
    elif computer =="Rock":
        if player == "Paper":
            print("YOU WIN!!", player, "covers" , computer)
        elif player == "Scissors":
            print("YOU LOSE!!", computer, "smashes" , player)

    elif computer == "Paper":
        if player == "Rock":
                  print("YOU LOSE!!", computer, "covers" , player)
        elif player == "Scissors":
            print("YOU WIN!!", player, "cuts" , computer)

    elif computer =="Scissors":
        if player=="Rock":
                    print("YOU WIN!!", player, "smashes" , computer)
        elif player == "Paper":
            print("YOU LOSE!!", computer, "cuts" , player)
    else:
         print("This is not a valid word... Please check your spelling")
    player==False
