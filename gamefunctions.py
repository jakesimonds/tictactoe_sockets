'''
Jake Simonds
CS 5700
HW4
gamefunctions.py
'''

import tictactoe
import tictactoed
import random


def checkBoard(position):
    if len(position) != 10:
        return -1
    for i in range(1, 10):
        if position[i] != 'X' or position[i] != 'O' or position[i] != 'N':
            return -1
    return 0


def printBoard(position):
    position_copy = ""
    for i in range(len(position)):
        if position[i] == 'N':
            position_copy += ' '
        else:
            position_copy += position[i]
    print("\n\n")
    print(position_copy[1] + " | " + position_copy[2] + " | " + position_copy[3])
    print("---------")
    print(position_copy[4] + " | " + position_copy[5] + " | " + position_copy[6])
    print("---------")
    print(position_copy[7] + " | " + position_copy[8] + " | " + position_copy[9])
    print("\n\n")
def makeMove(position, player_char):
    move = -1
    #while move < 1 or move > 9:
    while move != 1 and move != 2 and move != 3 and move != 4 and move != 5 and move != 6 and move != 7 and move != 8 and move != 9:
        move = int(input("Enter a move: "))
        if move < 1 or move > 9:
            print("invalid move, has to be 1-9, try again!")
    while position[move] != 'N':
        move = int(input("That one was taken! Try again\n"))
    #position[move] = player_char
    old_position = position
    new_position = position[:move] + player_char + position[move+1:]
    return new_position


def CompMakeMove(position, player_char):
    move = -1
    if player_char == 'X':
        opponent_char = 'O'
    else:
        opponent_char = 'X'

    if position[1] == player_char and position[2] == player_char and position[3] == 'N':
        move = 3
    elif position[1] == player_char and position[3] == player_char and position[2] == 'N':
        move = 2
    elif position[2] == player_char and position[3] == player_char and position[1] == 'N':
        move = 1


    elif position[4] == player_char and position[5] == player_char and position[6] == 'N':
        move = 6
    elif position[4] == player_char and position[6] == player_char and position[5] == 'N':
        move = 5
    elif position[5] == player_char and position[6] == player_char and position[4] == 'N':
        move = 4


    elif position[7] == player_char and position[8] == player_char and position[9] == 'N':
        move = 9
    elif position[7] == player_char and position[9] == player_char and position[8] == 'N':
        move = 8
    elif position[8] == player_char and position[9] == player_char and position[7] == 'N':
        move = 7


    elif position[1] == player_char and position[4] == player_char and position[7] == 'N':
        move = 7
    elif position[1] == player_char and position[7] == player_char and position[4] == 'N':
        move = 4
    elif position[4] == player_char and position[7] == player_char and position[1] == 'N':
        move = 1


    elif position[2] == player_char and position[5] == player_char and position[8] == 'N':
        move = 8
    elif position[2] == player_char and position[8] == player_char and position[5] == 'N':
        move = 5
    elif position[5] == player_char and position[8] == player_char and position[2] == 'N':
        move = 2


    elif position[3] == player_char and position[6] == player_char and position[9] == 'N':
        move = 9
    elif position[3] == player_char and position[9] == player_char and position[6] == 'N':
        move = 6
    elif position[6] == player_char and position[9] == player_char and position[3] == 'N':
        move = 3


    elif position[1] == player_char and position[5] == player_char and position[9] == 'N':
        move = 9
    elif position[1] == player_char and position[9] == player_char and position[5] == 'N':
        move = 5
    elif position[5] == player_char and position[9] == player_char and position[1] == 'N':
        move = 1


    elif position[3] == player_char and position[5] == player_char and position[7] == 'N':
        move = 7
    elif position[3] == player_char and position[7] == player_char and position[5] == 'N':
        move = 5
    elif position[5] == player_char and position[7] == player_char and position[3] == 'N':
        move = 3



    #DEFENSE

    elif position[1] == opponent_char and position[2] == opponent_char and position[3] == 'N':
        move = 3
    elif position[1] == opponent_char and position[3] == opponent_char and position[2] == 'N':
        move = 2
    elif position[2] == opponent_char and position[3] == opponent_char and position[1] == 'N':
        move = 1

    elif position[4] == opponent_char and position[5] == opponent_char and position[6] == 'N':
        move = 6
    elif position[4] == opponent_char and position[6] == opponent_char and position[5] == 'N':
        move = 5
    elif position[5] == opponent_char and position[6] == opponent_char and position[4] == 'N':
        move = 4

    elif position[7] == opponent_char and position[8] == opponent_char and position[9] == 'N':
        move = 9
    elif position[7] == opponent_char and position[9] == opponent_char and position[8] == 'N':
        move = 8
    elif position[8] == opponent_char and position[9] == opponent_char and position[7] == 'N':
        move = 7

    elif position[1] == opponent_char and position[4] == opponent_char and position[7] == 'N':
        move = 7
    elif position[1] == opponent_char and position[7] == opponent_char and position[4] == 'N':
        move = 4
    elif position[4] == opponent_char and position[7] == opponent_char and position[1] == 'N':
        move = 1

    elif position[2] == opponent_char and position[5] == opponent_char and position[8] == 'N':
        move = 8
    elif position[2] == opponent_char and position[8] == opponent_char and position[5] == 'N':
        move = 5
    elif position[5] == opponent_char and position[8] == opponent_char and position[2] == 'N':
        move = 2

    elif position[3] == opponent_char and position[6] == opponent_char and position[9] == 'N':
        move = 9
    elif position[3] == opponent_char and position[9] == opponent_char and position[6] == 'N':
        move = 6
    elif position[6] == opponent_char and position[9] == opponent_char and position[3] == 'N':
        move = 3

    elif position[1] == opponent_char and position[5] == opponent_char and position[9] == 'N':
        move = 9
    elif position[1] == opponent_char and position[9] == opponent_char and position[5] == 'N':
        move = 5
    elif position[5] == opponent_char and position[9] == opponent_char and position[1] == 'N':
        move = 1

    elif position[3] == opponent_char and position[5] == opponent_char and position[7] == 'N':
        move = 7
    elif position[3] == opponent_char and position[7] == opponent_char and position[5] == 'N':
        move = 5
    elif position[5] == opponent_char and position[7] == opponent_char and position[3] == 'N':
        move = 3

    #grab the middle if it's free
    elif position[5] == 'N':
        move = 5

    #opposite corner
    elif position[1] == opponent_char and position[9] == 'N':
        move = 9
    elif position[9] == opponent_char and position[1] == 'N':
        move = 1
    elif position[3] == opponent_char and position[7] == 'N':
        move = 7
    elif position[7] == opponent_char and position[3] == 'N':
        move = 3

    else:
        options = []
        for i in range(1,10):
            if position[i] == 'N':
                options.append(i)
        move = random.choice(options)

    old_position = position
    new_position = old_position[:move] + player_char + old_position[move+1:]
    return new_position

#1 is X win, 0 is Oh win, 2 is tie, -1 is game keeps going
def checkWin(position):
    if position[1] == 'X' and position[2] == 'X' and position[3] == 'X' or position[4] == 'X' and position[5] == 'X' and position[6] == 'X' or position[7] == 'X' and position[8] == 'X' and position[9] == 'X' or position[1] == 'X' and position[4] == 'X' and position[7] == 'X' or position[2] == 'X' and position[5] == 'X' and position[8] == 'X' or position[3] == 'X' and position[6] == 'X' and position[9] == 'X' or position[1] == 'X' and position[5] == 'X' and position[9] == 'X' or position[3] == 'X' and position[5] == 'X' and position[7] == 'X':
        return 1
    elif position[1] == 'O' and position[2] == 'O' and position[3] == 'O' or position[4] == 'O' and position[5] == 'O' and position[6] == 'O' or position[7] == 'O' and position[8] == 'O' and position[9] == 'O' or position[1] == 'O' and position[4] == 'O' and position[7] == 'O' or position[2] == 'O' and position[5] == 'O' and position[8] == 'O' or position[3] == 'O' and position[6] == 'O' and position[9] == 'O' or position[1] == 'O' and position[5] == 'O' and position[9] == 'O' or position[3] == 'O' and position[5] == 'O' and position[7] == 'O':
        return 0
    elif 'N' not in position:
        return 2
    else:
        return -1



def GameSummary(position):
    if checkWin(position) == 2:
        print('\nIt was a draw!\n')
    elif checkWin(position) == 1:
        print("\nXs won!\n")
    elif checkWin(position) == 0:
        print("\nOs won!\n")



def moveFirst(socket, id, Current_board):
    while True:
        if checkWin(Current_board) != -1:
            break
        #make a move
        Current_board = makeMove(Current_board, id)
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            socket.send(Current_board.encode())
            break

        # send it
        socket.send(Current_board.encode())
        # sent_ack = client_socket.recv(1024).decode()

        # receive it back
        Current_board = socket.recv(1024).decode()
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            break
    return Current_board

def moveFirstA(socket, id, Current_board):
    while True:
        if checkWin(Current_board) != -1:
            break
        #make a move
        Current_board = CompMakeMove(Current_board, id)
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            socket.send(Current_board.encode())
            break

        # send it
        socket.send(Current_board.encode())
        # sent_ack = client_socket.recv(1024).decode()

        # receive it back
        Current_board = socket.recv(1024).decode()
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            break
    return Current_board


def moveSecond(socket, id, Current_board):
    while True:
        # recieve it first
        Current_board = socket.recv(1024).decode()
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            break

        # make a move
        Current_board = makeMove(Current_board, id)
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            socket.send(Current_board.encode())
            break
        # send it back
        socket.send(Current_board.encode())
    return Current_board
    #print("moveSecond broke out of while loop")


def moveSecondA(socket, id, Current_board):
    while True:
        # recieve it first
        Current_board = socket.recv(1024).decode()
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            break

        # make a move
        Current_board = CompMakeMove(Current_board, id)
        printBoard(Current_board)

        if checkWin(Current_board) != -1:
            socket.send(Current_board.encode())
            break
        # send it back
        socket.send(Current_board.encode())
    return Current_board
    #print("moveSecond broke out of while loop")

def setUpGame():
    client_id_plus_first = input("Pick X or O, and choose if you'd like to move 1st or second. Format: 'X/O[space]1/2'\n")
    #First_or_Second = input("Do you want to go first or second? Enter 1 or 2\n")
    while len(client_id_plus_first) != 3 or client_id_plus_first[1] != ' ' or (client_id_plus_first[0] != 'X' and client_id_plus_first[0] != 'O') or (client_id_plus_first[2] != '1' and client_id_plus_first[2] != '2'):
        client_id_plus_first = input("Pick X or O, and choose if you'd like to move 1st or second. Format: 'X/O[space]1/2'\n")

    # if client_id_plus_first[0] == 'X':
    #     server_id = 'O'
    # else:
    #     server_id = 'X'
    #     client_id = '0'
    #
    # if client_id_plus_first[2] == '1':
    #     first = 'C'
    # #set up as else to hopefully keep game going when input is weird
    # else:
    #     first = 'S'

    return client_id_plus_first

def printInstructions():
    print("\nWelcome to Tic Tac Toe! You move by entering a number 1-9, which corresponds to positions in the grid (think about a numpad on a keyboard, it's that format).")
    print("\nClient will decide: who is X/O, who will go first, whether to play again\n")

# CLIENT ONLY FUNCTION
def checkToPlayAgain():
    # check if they want to play again
    play_again = ""
    while play_again != 'Y' and play_again != 'N':
        play_again = input("Would you like to play again? (Y/N): \n")
        if play_again != 'Y' and play_again != 'N':
            print("Need a Y or N")
    return play_again

