### Tic Tac Toe Project Description 

This was an academic project where we created client and server files to play Tic Tac Toe over web sockets. In a simpler world you could do this over a network, but with security being complicated this just works best when you both are on the same LAN, if I remember correctly. You can also just play yourself over two terminal windows.  

Also built an autoplayer that does not play perfectly, because it turns out there's more steps than you'd think to coding up an optimal playing agent. Kinda fun (I think) to try to beat it. Isn't too tricky. 

### Tic Tac Toe how to run

Boot up the server: 
```commandline
python3 ./ttt.py -s
```
Server will then display on command line the port number. 

Boot up the client: 
```commandline
python3 ./ttt.py -c <server IP> <server port>
```
You can get the server IP by running ifconfig or 'ipconfig getifaddr en0' on mac. 127.0.0.1 can be used when testing locally on the same machine in two terminal windows. 

## Autoplay

If you would like have the computer make moves for either client or server, add 'A' to the -s or -c flags. 

```commandline
python3 ./ttt.py -sA
```

```commandline
python3 ./ttt.py -c <server IP> <server port>
```

I find best results for autoplay are to boot up the server with -sA, and then play client as human(because client makes decisions). 

## Brief Description of Code:
Go to more_details.pdf for more granular details. But in brief this is written in python, the client makes all decisions (X/O, who goes first, whether to play again), 
the game state is passed back and forth over the wire as a 10-character string. The first character of the string is a dummy variable 'G' (for 'Game', it makes indexing a little easier/more intuitive (1-9 instead of 0-8)), 
then 'X' = X, 'O' = O, 'N' = empty square. 

Example: 'GXXOOXOONN' would correspond to the following board/gamestate: 
```
 X  |  X  |  O
 -------------
 O  |  X  |  O
 -------------
 O  |     |  
```


'GNNNNNNNNN' would correspond to an empy board. 

