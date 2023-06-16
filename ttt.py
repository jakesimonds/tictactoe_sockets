import sys
from tictactoe import run_client
from tictactoed import run_server
from tictactoeA import run_clientA
from tictactoedA import run_serverA

def main():
    if len(sys.argv) < 2:
        print("Usage: python ttt.py [-c | -s]")
        sys.exit(1)

    flag = sys.argv[1]

    if flag == '-c' and len(sys.argv) < 4:
        print("Usage: python ttt.py -c <ip> <port>")
    elif flag == '-c':
        run_client(sys.argv[2], int(sys.argv[3]))
    elif flag == '-s':
        run_server()
    elif flag == '-sA':
        run_serverA()
    elif flag == '-cA':
        run_clientA(sys.argv[2], int(sys.argv[3]))
    else:
        print("Invalid flag. Use -c for client or -s for server.")
        sys.exit(1)

if __name__ == '__main__':
    main()
