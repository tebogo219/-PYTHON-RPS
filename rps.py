import random


for i in range(5):
    r = int(random.randrange(4))
    
    answer = int(input("kindly select rock = 1, paper = 2, scissors = 3 "))
    if answer != "1" or "2" or "3":
        print("wrong input the game will stop now as you dont follow instructions")
        quit()
    if answer == 1:
        if r == 1:
            print("you chose rock and the computer chose rock so there is no winner")
        elif r == 2:
            print("computer wins because paper covers rock")
        else:
            print("you win because rock breaks scissors")
       
    if answer == 2:
        if r == 1:
            print("you win because paper covers rock ")
        elif r == 2:
            print("you chose paper and the computer chose paper so there is no winner ")
        else:
            print("computer wins because scissors cuts paper")
        
    if answer == 3:
        if r == 1:
            print("computer wins because rock breaks scissors")
        elif r == 2:
            print("you win because scissors cut paper ")
        else:
            print("you chose scissors and the computer chose scissors so there is no winner ")
   
        
   