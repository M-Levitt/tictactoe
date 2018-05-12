#used with help from codecademy's battleship game
import time
import random
design = []
def board(): #creates board
    for i in range(0,3):
        design.append(["#"] * 3)

turn_decider = random.randint(0, 1) #determines who will go first
spots = [] #list that will contain used up spots on the board
turn = 1 #game starts at turn 1
def draw_design(design): #creates layout of board
    for row in design:
        print (" ".join(row))

print("Hello there and welcome to this tictactoe game.")#introduces player to the game, this is what the user will first see when they start the program
def mode_selecter():
    question = input("What gamemode would you like to play? \nType single for single player.\nType multi for multiplayer.\nType instructions for instructions.")
    if question == "single":
        print("_____________________________________________")
        single_player()
    elif question == "multi":
        print("_____________________________________________")
        multi_player()
    elif question == "instructions":
        instructions()
        mode_selecter()
    else:
        print("Please select a mode")
        print("_____________________________________________")
        mode_selecter()

def instructions():
    print("_____________________________________________")
    print("The board is constructed like this: ")
    board()
    draw_design(design)
    print("To begin the game, please select a gamemode when the game prompts you too.")
    print("If you play single player, you'll be playing against the computer. \nIf you play multiplayer, you'll be playing against a human opponent.")
    print("The game will randomly decide who gets to go first regardless of what mode you select.")
    print("To make your moves, first select a row, and then a column.")
    print("This game is coded, so the rows and columns start from 0 and end at 2. \nThis means that a move such as row 3 and column 3 is invalid.")
    print("For reference, to select the middle square, you would input row 1, column 1, instead of row 2, column 2.")
    print("Once the game has concluded, the program will wait for 2 seconds. Then it will end.\nIf you'd like to play another game, run the the program again in the terminal.")
    print("_____________________________________________")

def single_player():#code that will execute a single player game(game with computer)
    del design[:]
    board()
    if turn_decider == 0:
        print("You get to go first")
    if turn_decider == 1:
        print("The computer gets to go first")
    def turns():
        while turn in range(1, 10):
            if turn_decider == 0:
                if turn %2 == 0:
                    computer_turn()
                    single_check()
                elif turn %2 == 1:
                    player_turn()
                    single_check()
            elif turn_decider == 1:
                if turn %2 == 0:
                    player_turn()
                    single_check()
                elif turn %2 == 1:
                    computer_turn()
                    single_check()
            turns()
            break
    turns()

def multi_player():#code that will execute a multiplayer game(game with other human player)
    del design[:]
    board()
    if turn_decider == 0:
        print("Player 1 will go first")
    if turn_decider == 1:
        print("Player 2 will go first")
    def turns():
        while turn in range(1, 10):
            if turn_decider == 0:
                if turn %2 == 0:
                    multi_turn()
                    multi_check()
                elif turn %2 == 1:
                    multi_turn()
                    multi_check()
            elif turn_decider == 1:
                if turn %2 == 0:
                    multi_turn()
                    multi_check()
                elif turn %2 == 1:
                    multi_turn()
                    multi_check()
            turns()
            break
    turns()
#marks where single player code is
def computer_turn():#code for the computer's turn
    global turn
    global turn_decider
    global spots
    if turn == 1:
        x = 1
        y = 1
        lis = [x, y]
        spots.append(lis)
        print("Turn", turn)
        print("The computer will make its move.")
        design[x][y] = "x"
        draw_design(design)
        turn += 1
    elif turn in range(2, 10):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        lis = [x, y]
        if lis in spots:
            computer_turn()
        else:
            spots.append(lis)
            if turn_decider == 1:
                if turn % 2 == 0: 
                    design[x][y] = "o"
                elif turn % 2 == 1:
                    design[x][y] = "x"
            elif turn_decider == 0:
                if turn % 2 == 0:
                    design[x][y] = "o"
                elif turn % 2 == 1:
                    design[x][y] = "x"
            print("Turn", turn)
            print("The computer will make its move.")
            draw_design(design)
            turn += 1

def player_turn():#code for the player's turn
    global turn
    global spots
    global turn_decider
    print("Turn", turn)
    if turn == 1:
        draw_design(design)
    try:
        print("It's your turn to make your move.")
        x = int(input("Select a row to mark your move: "))
        y = int(input("Select a column to mark your move: "))
        lis = [x, y]
        if x < 0 or y < 0 or x > 2 or y > 2:
            print("That's not on the board. \nPlease select a different spot.")
            player_turn()
        elif lis in spots:
            print("That spot is already taken. \nPlease select a different spot.")
            player_turn()
        else:
            spots.append(lis)
            if turn_decider == 1:
                design[x][y] = "o"
            elif turn_decider == 0:
                design[x][y] = "x"
            draw_design(design)
            turn += 1
    except (ValueError):
        print("Please input a number.")
        player_turn()

def single_check():#check if the game has been won, will only execute if requirements are met
    if turn_decider == 0:
        if design[0][0] == "x" and design[0][1] == "x" and design[0][2] == "x" or \
        design[1][0] == "x" and design[1][1] == "x" and design[1][2] == "x" or \
        design[2][0] == "x" and design[2][1] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][0] == "x" and design[2][0] == "x" or \
        design[0][1] == "x" and design[1][1] == "x" and design[2][1] == "x" or \
        design[0][2] == "x" and design[1][2] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][1] == "x" and design[2][2] == "x" or \
        design[0][2] == "x" and design[1][1] == "x" and design[2][0] == "x": #user wins
            print("You have won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif design[0][0] == "o" and design[0][1] == "o" and design[0][2] == "o" or \
        design[1][0] == "o" and design[1][1] == "o" and design[1][2] == "o" or \
        design[2][0] == "o" and design[2][1] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][0] == "o" and design[2][0] == "o" or \
        design[0][1] == "o" and design[1][1] == "o" and design[2][1] == "o" or \
        design[0][2] == "o" and design[1][2] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][1] == "o" and design[2][2] == "o" or \
        design[0][2] == "o" and design[1][1] == "o" and design[2][0] == "o": #computer wins
            print("The computer has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif turn == 10:
            print("The game was a draw!")
            del spots[:]
            time.sleep(2)
            quit()
    elif turn_decider == 1:
        if design[0][0] == "o" and design[0][1] == "o" and design[0][2] == "o" or \
        design[1][0] == "o" and design[1][1] == "o" and design[1][2] == "o" or \
        design[2][0] == "o" and design[2][1] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][0] == "o" and design[2][0] == "o" or \
        design[0][1] == "o" and design[1][1] == "o" and design[2][1] == "o" or \
        design[0][2] == "o" and design[1][2] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][1] == "o" and design[2][2] == "o" or \
        design[0][2] == "o" and design[1][1] == "o" and design[2][0] == "o": #user wins
            print("You have won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif design[0][0] == "x" and design[0][1] == "x" and design[0][2] == "x" or \
        design[1][0] == "x" and design[1][1] == "x" and design[1][2] == "x" or \
        design[2][0] == "x" and design[2][1] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][0] == "x" and design[2][0] == "x" or \
        design[0][1] == "x" and design[1][1] == "x" and design[2][1] == "x" or \
        design[0][2] == "x" and design[1][2] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][1] == "x" and design[2][2] == "x" or \
        design[0][2] == "x" and design[1][1] == "x" and design[2][0] == "x": #computer wins
            print("The computer has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif turn == 10:
            print("The game was a draw!")
            del spots[:]
            time.sleep(2)
            quit()
#marks where multiplayer code is
def multi_turn():#basically like a player_turn in single player, but it's done multiple times to simulate player 1 and player 2 turns
    global turn
    global spots
    global turn_decider
    print("Turn", turn)
    if turn == 1:
        draw_design(design)
    try:
        if turn_decider == 0:    
            if turn % 2 == 0:
                print("It's player 2's turn.")
            elif turn % 2 == 1:
                print("It's player 1's turn.")
        elif turn_decider == 1:
            if turn % 2 == 0:
                print("It's player 1's turn.")
            elif turn % 2 == 1:
                print("It's player 2's turn.")
        x = int(input("Select a row to mark your move: "))
        y = int(input("Select a column to mark your move: "))
        lis = [x, y]
        if x < 0 or y < 0 or x > 2 or y > 2:
            print("That's not on the board. \nPlease select a different spot.")
            multi_turn()
        elif lis in spots:
            print("That spot is already taken. \nPlease select a different spot.")
            multi_turn()
        else:
            spots.append(lis)
            if turn % 2 == 0:
                design[x][y] = "o"
            elif turn % 2 == 1:
                design[x][y] = "x"
            draw_design(design)
            turn += 1
    except (ValueError):
        print("Please input a number.")
        multi_turn()

def multi_check():#check like single_check, only formatted for multiplayer
    if turn_decider == 0:
        if design[0][0] == "x" and design[0][1] == "x" and design[0][2] == "x" or \
        design[1][0] == "x" and design[1][1] == "x" and design[1][2] == "x" or \
        design[2][0] == "x" and design[2][1] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][0] == "x" and design[2][0] == "x" or \
        design[0][1] == "x" and design[1][1] == "x" and design[2][1] == "x" or \
        design[0][2] == "x" and design[1][2] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][1] == "x" and design[2][2] == "x" or \
        design[0][2] == "x" and design[1][1] == "x" and design[2][0] == "x": #user wins
            print("Player 1 has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif design[0][0] == "o" and design[0][1] == "o" and design[0][2] == "o" or \
        design[1][0] == "o" and design[1][1] == "o" and design[1][2] == "o" or \
        design[2][0] == "o" and design[2][1] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][0] == "o" and design[2][0] == "o" or \
        design[0][1] == "o" and design[1][1] == "o" and design[2][1] == "o" or \
        design[0][2] == "o" and design[1][2] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][1] == "o" and design[2][2] == "o" or \
        design[0][2] == "o" and design[1][1] == "o" and design[2][0] == "o": #computer wins
            print("Player 2 has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif turn == 10:
            print("The game was a draw!")
            del spots[:]
            time.sleep(2)
            quit()
    elif turn_decider == 1:
        if design[0][0] == "o" and design[0][1] == "o" and design[0][2] == "o" or \
        design[1][0] == "o" and design[1][1] == "o" and design[1][2] == "o" or \
        design[2][0] == "o" and design[2][1] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][0] == "o" and design[2][0] == "o" or \
        design[0][1] == "o" and design[1][1] == "o" and design[2][1] == "o" or \
        design[0][2] == "o" and design[1][2] == "o" and design[2][2] == "o" or \
        design[0][0] == "o" and design[1][1] == "o" and design[2][2] == "o" or \
        design[0][2] == "o" and design[1][1] == "o" and design[2][0] == "o": #user wins
            print("Player 1 has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif design[0][0] == "x" and design[0][1] == "x" and design[0][2] == "x" or \
        design[1][0] == "x" and design[1][1] == "x" and design[1][2] == "x" or \
        design[2][0] == "x" and design[2][1] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][0] == "x" and design[2][0] == "x" or \
        design[0][1] == "x" and design[1][1] == "x" and design[2][1] == "x" or \
        design[0][2] == "x" and design[1][2] == "x" and design[2][2] == "x" or \
        design[0][0] == "x" and design[1][1] == "x" and design[2][2] == "x" or \
        design[0][2] == "x" and design[1][1] == "x" and design[2][0] == "x": #computer wins
            print("Player 2 has won the game!")
            del spots[:]
            time.sleep(2)
            quit()
        elif turn == 10:
            print("The game was a draw!")
            del spots[:]
            time.sleep(2)
            quit()

mode_selecter()#starts the program

