import random
winning_number= random.randint(1.100)
guess=1
number=int(input("guess a number between 1 and 100 : "))
game_over=False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guessedthis number in {guess} times ")
        game_over = Truee
    else:
        if number < winning_number:
            print("too low")
        else:
            if number>winning_number:
                print("too high")

        guess += 1
        number=int(input("guess again : "))
        #DRY _ don't repeat yourself