"""
Python 2
2-player Battleship
Author: Pairode Jaroensri
Last visited: August 2016
"""
import os
os.system('clear')
board1 = [] # Show to the other player
board1_content = [] # Show to owner
board2 = []
board2_content = []

for x in range(8):
    board1.append(["O"] * 8)
    board1_content.append(["O"] * 8)
    board2.append(["O"] * 8)
    board2_content.append(["O"] * 8)

def print_board(board):
    for row in board:
        print " ".join(row)

#cv bb ca dd
#Place the ship on the board after the user has entered values
def place_ship(board, len_ship):
    undo_board = [x for x in board]
    repeat = True
    while repeat:
        board = undo_board
        if len_ship == 5: #Tell ship class
            print "Place your aircraft carrier."
        elif len_ship == 4:
            print "Place your battleship"
        elif len_ship == 3:
            print "Place your cruiser"
        elif len_ship == 2:
            print "Place your destroyer"
        print_board(board)
        orientation = raw_input("Choose your orientation. V = verticle; H = horizontal: ")
        if orientation == 'v' or orientation == 'V': #vertical
            x = input("X coordinate: ") - 1
            y = input("Y coordinate: ") - 1
            if x <= len(board) and y + len_ship <= len(board): #Check if the ship is on the board.
                space = [] #Check if the coordinate is empty.
                for i in range(len_ship):
                    space.append(board[y+i][x])
                space.sort()
                check = []
                index = 0
                while index < len(space):
                    if index != 0 and space[index] == space[index-1]:
                        index += 1
                    else:
                        check.append(space[index])
                        index += 1
                #print "check is: ", check
                if len(check) == 1 and check[0] != 'S': #Okay to place the ship.
                    for i in range(len_ship):
                        board[y+i][x] = 'S'
                    print "Ship placed"
                    print_board(board)
                    repeat = False
                else:
                    print "The coordinates are not empty. Try again."
            else:
                print "That is not on the board. Try again."

        elif orientation == 'h' or orientation == 'H': #horizontal
            x = input("X coordinate: ") - 1
            y = input("Y coordinate: ") - 1
            if y <= len(board) and x + len_ship <= len(board): #Check if the ship is on the board.
                space = [] #Check if the coordinate is empty.
                for i in range(len_ship):
                    space.append(board[y][x+i])
                space.sort()
                check = []
                index = 0
                while index < len(space):
                    if index != 0 and space[index] == space[index-1]:
                        index += 1
                    else:
                        check.append(space[index])
                        index += 1
                print "check is: ", check
                if len(check) == 1 and check[0] != 'S': #Okay to place the ship.
                    for i in range(len_ship):
                        board[y][x+i] = 'S'
                    print "Ship placed"
                    print_board(board)
                    repeat = False
                else:
                    print "The coordinates are not empty. Try again."
            else:
                print "That is not on the board. Try again."
        else:
            print "Invalid orientation. Try again."
            
print "Kim's Battleship v.2.0 build 072616"
print "Player1's turn to place the ships."
place_ship(board1_content, 5)
place_ship(board1_content, 4)
place_ship(board1_content, 3)
place_ship(board1_content, 2)
go_on = raw_input("Press enter to continue.")
os.system('clear')
print "Player2's turn to place the ships."
place_ship(board2_content, 5)
place_ship(board2_content, 4)
place_ship(board2_content, 3)
place_ship(board2_content, 2)
go_on = raw_input("Press enter to start the game.")
os.system('clear')
player = 1
game_on = True

while game_on:

    while player == 1 and game_on:
        print "Player1's turn"
        print_board(board2)
        x_p1 = int(raw_input("Guess X:")) - 1
        y_p1 = int(raw_input("Guess Y:")) - 1
        if board2_content[y_p1][x_p1] == 'S':
            print "Hit!"
            board2[y_p1][x_p1] = 'H' #Mark the hit spot on board2.
        elif board2[y_p1][x_p1] == 'X':
            print "You've already guessed that spot."
        else:
            print "Miss"
            board2[y_p1][x_p1] = 'X' #Mark the miss spot on board2.
            player = 2
        hit_count_p2 = 0 #Number of hits player2 received.
        for row in board2: #Check if player2 has any ship left.
            for ele in row:
                if ele == 'H':
                    hit_count_p2 += 1
        if hit_count_p2 == 14:
            winner = 1
            game_on = False
        else:
            print_board(board2)
            go_on = raw_input("Press enter to continue.")
            os.system('clear')

    while player == 2 and game_on:
        print "Player2's turn"
        print_board(board1)
        x_p2 = int(raw_input("Guess X:")) - 1
        y_p2 = int(raw_input("Guess Y:")) - 1
        if board1_content[y_p2][x_p2] == 'S':
            print "Hit!"
            board1[y_p2][x_p2] = 'H'
        elif board1[y_p2][x_p2] == 'X':
            print "You've already guessed that spot."
        else:
            print "Miss"
            board1[y_p2][x_p2] = 'X'
            player = 1
        hit_count_p1 = 0 #Number of hits player1 received.
        for row in board1:
            for ele in row:
                if ele == 'H':
                    hit_count_p1 += 1
        if hit_count_p1 == 14:
            winner = 2
            game_on = False
        else:
            print_board(board1)
            go_on = raw_input("Press enter to continue.")
            os.system('clear')

print "Player%i win!" % winner
answer = raw_input("Would you like to see the boards?(Y/N): ")
while answer == 'y' or answer == 'Y' or answer == "":
    print "Options:\n 1: Player 1's guesses\n 2: Player 2 ships' positions\n 3: Player 2's guesses\n 4: Player 1 ships' positions\n 5: Exit\n"
    choice = raw_input()
    if choice == '1':
        print_board(board2)
    elif choice == '2':
        print_board(board2_content)
    elif choice == '3':
        print_board(board1)
    elif choice == '4':
        print_board(board1_content)
    else:
        answer = 'N'
else:
    print "Thank you for playing!"
