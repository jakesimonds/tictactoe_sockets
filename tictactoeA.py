'''
Jake Simonds
CS 5700
HW4 due 4/16
tictactoe.py, client
'''
import socket
import sys
import gamefunctions
import random
def run_clientA(IP_ADDRESS_, PORT_NUM_):
    current_board = 'GNNNNNNNNN'

    IP_ADDRESS = IP_ADDRESS_
    PORT_NUM = PORT_NUM_

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_ADDRESS, PORT_NUM))

    print("\n\nServer and Client are connected, and may begin game. \n\n")

    while True:
        #server_id_plus_first = gamefunctions.setUpGame()
        cases = ['X 1', 'X 2', 'O 1', 'O 2'] # four possible options for user input (no user, duh)
        server_id_plus_first = random.choice(cases)
        server.send(server_id_plus_first.encode()) #send 'X' or 'O'
        #server.send(first.encode()) #send who goes first 'C' or 'S'
        client_id = server_id_plus_first[0]
        first = server_id_plus_first[2]


        # client_id, server_id, first = gamefunctions.setUpGame()
        #
        # server.send(server_id.encode()) #send 'X' or 'O'
        # server.send(first.encode()) #send who goes first 'C' or 'S'
        gamefunctions.printInstructions()
        if first == '1':
            print('Client goes first')
            current_board = gamefunctions.moveFirstA(server, client_id, current_board)
        else:
            print('Server goes first')
            current_board = gamefunctions.moveSecondA(server, client_id, current_board)


        gamefunctions.GameSummary(current_board)
        current_board = 'GNNNNNNNNN' #reset board

        # check if they want to play again
        options_play_again = ['Y', 'N']
        play_again = random.choice(options_play_again)
        #play_again = gamefunctions.checkToPlayAgain()

        if play_again == 'Y':
            server.send('Y'.encode())
        else:
            play_again = 'N' #making it so anything besides a 'Y' becomes 'N'
            server.send(play_again.encode())
            break

    server.close()
    print("\n Games over, connection closed. \n")