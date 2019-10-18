from random import randint

def show_board(grid):
    print("Board: ")
    for i in range(3):
        for j in range(3):
            print("\t", grid[i*3 + j], end=" ")
        print()

def check_win(grid, check):
    if grid[0:3] == [check]*3 or grid[3:6] == [check]*3 or grid[6:9] == [check]*3:
        return True
    for i in range(3):
        if grid[i] == check and grid[i + 3] == check and grid[i + 6] == check:
            return True
    if grid[0] == check and grid[4] == check and grid[8] == check:
        return True
    if grid[2] == check and grid[4] == check and grid[6] == check:
        return True
    return False

def text_based_tic_tac_toe():
    two_persons = input('Hi, please enter mode (Y: To play against computer or N: 2 players): ').upper()
    player1_name = input("Enter Player 1's name: ")


    if player1_name == "":
        player1_name = "Player 1"
    player2_name = "Computer"
    if two_persons != "Y":
        player2_name = input("Enter Player 2's name: ")
    if player2_name == "":
        player2_name = "Player 2"

    player1_name = player1_name.capitalize()
    player2_name = player2_name.capitalize()

    pl1_choice = input("Player 1's choice (X/O): ").upper()
    pl2_choice = None
    if pl1_choice == "X":
        pl2_choice = "O"
    elif pl1_choice == "O":
        pl2_choice = "X"
    else:
        pl1_choice = "X"
        pl2_choice = "O"
    

    occupied = ["-" for _ in range(9)]
    num_unoccupied = 9
    round_ = None
    round_choice = None

    toss = randint(0, 1)
    if toss:
        round_ = player1_name
        round_choice = pl1_choice
    else:
        round_ = player2_name
        round_choice = pl2_choice
    print("We will now randomly decide who begins!")
    while num_unoccupied:
        str1 = round_ + "'s turn(enter: #row(1-3) #column(1-3)):"
        input_ = None
        if round_ == "Computer":
            print("Computer's turn")
            ans = randint(0, 8)
            while occupied[ans] != "-":
                ans = randint(0, 8)
            input_ = ans
        else:
            try:
                i, j = tuple(map(int, input(str1).strip().split()))
                input_ = i*3 + j - 4
                while input_ < 0 or input_ > 8 or occupied[input_] != "-":
                    print("Invalid input!!!")
                    i, j = tuple(map(int, input(str1).strip().split()))
                    input_ = i*3 + j - 4
            except:
                try:
                    print("Format is #row(1-3), #column(1-3)!")
                    i, j = tuple(map(int, input(str1).strip().split()))
                    input_ = i*3 + j - 4
                    while input_ < 0 or input_ > 8 or occupied[input_] != "-":
                        print("Invalid input!!!")
                        i, j = tuple(map(int, input(str1).strip().split()))
                except:
                    break
                    input_ = i*3 + j - 4
        occupied[input_] = round_choice
        num_unoccupied -= 1

        show_board(occupied)
        if check_win(occupied, round_choice):
            print("\n***\n"+ round_ +" won!!!!!!!!!!!\n***\n")
            again = input("Would you like to play again!(Y/n): ").upper()
            if again == "Y":
                text_based_tic_tac_toe()
            break
        if round_ == player1_name:
            round_ = player2_name
            round_choice = pl2_choice
        else:
            round_ = player1_name
            round_choice = pl1_choice
    else:
        print("Tie between: ", player1_name, " and ", player2_name)
        again = input("Would you like to play again!(Y/n): ").upper()
        if again == "Y":
            text_based_tic_tac_toe()


text_based_tic_tac_toe()
        

                
    
