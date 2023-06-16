'''
Jake Simonds
CS 5700
HW4 due 4/16
tictactoed.py, server
'''
import socket
import gamefunctions
import random

def run_serverA():
    current_board = "GNNNNNNNNN"

    PORT_NUM = random.randint(5000,10000)
    init_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    init_socket.bind(('', PORT_NUM)) # empty string so it listens on all available interfaces
    init_socket.listen(2)

    print("Server has started up, is waiting for client. PORT:" + str(PORT_NUM))
    print("\nListening...") # establishing connection

    client_socket, addr = init_socket.accept()
    print("\nGot a connection from %s" % str(addr))

    while True:
        #print("test -1")
        print("\nWaiting for client to decide who's X and O...\n")

        server_id_plus_first = client_socket.recv(1024).decode() # receive 'X' or 'O'
        if server_id_plus_first[0] == 'X':
            server_id = 'O'
        else:
            server_id = 'X'
        first = server_id_plus_first[2]


        #server_id = client_socket.recv(1024).decode() # recieve 'X' or 'O'
        #server_id = client_socket.recv(1024)
        print("\nServer is: " + server_id)
        #print("test 0 ")
        #first = client_socket.recv(1024).decode() #recieve 'C' or 'S' for who goes first
        gamefunctions.printInstructions()
        if first == '1':
            print('\nClient goes first')
            current_board = gamefunctions.moveSecondA(client_socket, server_id, current_board)
        else:
            print('\nServer goes first')
            current_board = gamefunctions.moveFirstA(client_socket, server_id, current_board)

        gamefunctions.GameSummary(current_board)
        current_board = "GNNNNNNNNN" #reset board

        play_again = client_socket.recv(1024).decode()

        if play_again == 'N':
            break
        else:
            print("\nClient wants to play again! \n")

    client_socket.close()  # close the socket
    init_socket.close()
    print("Client has ended the game. Sockets are closed. Thank you for playing!") #NOT REACHING HERE
