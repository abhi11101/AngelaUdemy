print("Welcome to the Treasure Island")

move1 = input("left or right?L or R\n")

if move1 == 'L':
    move2 = input("Swim or Wait? S or W\n")
    if move2 == 'W':
        move3 = input("Which door? R, B or Y\n")
        if move3 == 'Y':
            print("You Win!!!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
