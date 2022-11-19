while(True):
    import random

    def gameWin(comp, You):
        if comp == You:
            return None
        elif comp == 's':
            if You == 'g':
                return True
            elif You == 'w':
                return False
        elif comp == 'g':
            if You == 's':
                return False
            elif You == 'w':
                return True
        elif comp == 'w':
            if You == 's':
                return True
            elif You == 'g':
                return False

    print("Computer turn : snake(s), water(w) or gun(g)?")
    random_number= random.randint(1,3)
    if random_number == 1:
        comp = 's'
    elif random_number == 2:
        comp = 'w'
    elif random_number == 3:
        comp = 'g'
    You = input("Your turn : snake(s), water(w) or gun(g) or press (q) to quit:  ")
    if You == 'q':
        break
    a = gameWin(comp, You)

    print(f"comp chose : {comp}")
    print(f"You chose : {You}")
    if a == None:
        print("The Game is tie!")
    elif a == True:
        print("Congratulation! You Win!")
    else:
        print("You lose!")
print('Thanks for playing this game!')