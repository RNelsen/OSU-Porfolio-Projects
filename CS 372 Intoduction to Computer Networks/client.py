# Name: Daniel Reid Nelsen
# Class: CS 372 Intro to Networking
# Project: Portfolio Project 
# Due: 12/7/2023
# Description: This is the client side of server-chat portfolio project.  This
#              file should be started after the server has been started.


import socket

# Set global variables
MAXDATALENGTH = 4096
IP = "127.0.0.1"
PORT = 4999

# Setup client socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print(f"Client connected to server at {IP} on port {PORT}")


first_message = client.recv(MAXDATALENGTH).decode('utf-8')

if first_message != "":
    print(first_message)


def main():
    '''
    Main function of the client to interact with the server chat program.  
    Options for input are listed below
    /game: starts trivia game
    /q: closes connection with server and shuts down program
    '''
    finished = False

    while not finished:

        send_message = input("Enter Input > ")

        if send_message == "/game":
            client.send(send_message.encode('utf-8'))
            gaming()
            send_message = "Finished with game"

        if send_message == "/q":
            client.send(send_message.encode('utf-8')) 
            print("Client disconnecting")
            client.close()
            break

        while send_message == "":
            print("Can't send empty message please try again")
            send_message = input("Enter Input > ")

        client.send(send_message.encode('utf-8'))

        recv_message = client.recv(MAXDATALENGTH).decode('utf-8')
        print(recv_message)
        
        if recv_message == "/q":
            print("Server disconnecting.  Shutting down now.")
            client.close()
            break

def gaming():
    '''
    This is the trivia game function to handle receiving and answering questions.
    /endgame: will end the game
    /score: will show the current score
    
    '''

    while True:
    
        recv_message = client.recv(MAXDATALENGTH).decode('utf-8')
        print(recv_message)

        send_message = input("Enter Input > ")
        client.send(send_message.encode('utf-8'))
        recv_message = client.recv(MAXDATALENGTH).decode('utf-8')
        print(recv_message)

        if send_message == "/endgame":
            break


if __name__ == "__main__":
    main()