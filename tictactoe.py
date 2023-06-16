'''
Jake Simonds
CS 5700
HW4 due 4/16
tictactoe.py, client
'''
import socket
import sys
import gamefunctions
def run_client(IP_ADDRESS_, PORT_NUM_):
    current_board = 'GNNNNNNNNN'

    IP_ADDRESS = IP_ADDRESS_
    PORT_NUM = PORT_NUM_

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_ADDRESS, PORT_NUM))

    print("\n\nServer and Client are connected, and may begin game. \n\n")

    while True:
        server_id_plus_first = gamefunctions.setUpGame()

        server.send(server_id_plus_first.encode()) #send 'X' or 'O'
        #server.send(first.encode()) #send who goes first 'C' or 'S'
        client_id = server_id_plus_first[0]
        first = server_id_plus_first[2]

        gamefunctions.printInstructions()
        if first == '1':
            print('Client goes first')
            current_board = gamefunctions.moveFirst(server, client_id, current_board)
        else:
            print('Server goes first')
            current_board = gamefunctions.moveSecond(server, client_id, current_board)


        gamefunctions.GameSummary(current_board)
        current_board = 'GNNNNNNNNN' #reset board

        # check if they want to play again
        play_again = gamefunctions.checkToPlayAgain()

        if play_again == 'Y':
            server.send('Y'.encode())
        else:
            play_again = 'N' #making it so anything besides a 'Y' becomes 'N'
            server.send(play_again.encode())
            break

    server.close()
    print("\n Games over, connection closed. \n")