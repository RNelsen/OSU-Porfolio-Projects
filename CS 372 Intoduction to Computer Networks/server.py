# Name: Daniel Reid Nelsen
# Class: CS 372 Intro to Networking
# Project: Portfolio Project 
# Due: 12/7/2023
# Description:  This project is a demonstration of a client-server chat. This file 
#               This file holds the server side for the project.  It will open
#               a connection to connect to use python sockets and the client is 
#               able to interact and start a simple trivia game.  Stopping the 
#               server will shutdown the server and terminate the connection. 
#               The chat function is turn-based and input is only available after
#               receiving a message from the other side of the chat.  During the
#               game the server will not accept input.  Only after exiting the 
#               game will the server allow input.


import socket

from triviagame import TriviaGame


# Code adapted from
# The Simplest Python Chat You Can Build
# https://www.youtube.com/watch?v=Ar94t2XhKzM
# Accessed 12/2/2023

# Setting global variables
MAXDATALENGTH = 4096
IP = "127.0.0.1"
PORT = 4999

# Setup server object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen()

print(f"Server listening on {IP} and port {PORT}")

client, addr = server.accept()
print(f"Client connected on {addr[0]} and port {addr[1]}")

        
def main():
    '''
    This is the main function for the server.  Basic commands are listed below
    in the first_message variable. 
    '''

    finished = False
    send_message = ""

    first_message = "Welcome to the server-chat program.  Below are a few basic commands that you enter.  \r\n \
            \n \
            Commands:\r\n \
            /q: Quit chat program and shutdown\r\n \
            /game: Start a trivia game \r\n \
            /endgame: End the game \r\n \
            /score: Shows current game score and percent correct answers \r\n\n \
            You need to wait for the prompt before you are able to send a message"


    client.send(first_message.encode('utf-8'))

    after_game = False

    while not finished:
            
        try:
            recv_message = client.recv(MAXDATALENGTH).decode('utf-8')
        except:
            pass

        print(recv_message)

        if send_message == '/q':
            print("Server disconnecting")
            server.close()
            break
        elif recv_message == '/q':
            print("Client disconnecting. Shutting down the server.")
            server.close()
            break
        
        if recv_message == '/game':
            gameOn()
            after_game = True
        
        if not after_game:
            send_message = input("Enter Input > ")

            while send_message == "":
                print("Can't send empty message, please try again")
                send_message = input("Enter Input > ")

            client.send(send_message.encode('utf-8'))

        after_game = False

def gameOn():
    '''
    This is the simple trivia game function.  Client will receive random questions from
    a list of trivia questions.  The client can end the game by typing /endgame
    or see the score by typing /score.  There are over 5,000 questions so 
    testing correct questions is best done by looking in the trivia_questions.json
    file....if you don't know the answer.
    '''

    game = TriviaGame()
    game.readQuestionsFromFile()

    while True:

        game.setQuestionAndAnswer()
        client.send(game.getQuestion().encode('utf-8'))

        recv_message = client.recv(MAXDATALENGTH).decode('utf-8')

        if recv_message == '/endgame':
            final_message = "Thanks for playing. The number of correctly answered questions was "  + \
                str(game.getNumRight()) + ". " + "Your percentage correct is " + \
                str(round(game.getScore(), 2)) + "%."
            client.send(final_message.encode('utf-8'))
            break
        elif recv_message == '/score':
            score = "Your current score\n" + "Correct Answers: " + str(game.getNumRight()) + "\n" \
            "Incorrect Answers: " + str(game.getNumAnswered() - game.getNumRight()) + "\n" \
            "Percentage: " + str(round(game.getScore(), 2)) + "\n"
            client.send(score.encode('utf-8'))
        else:
            if game.checkAnswer(recv_message):
                client.send("That's correct. Good Job!\n".encode('utf-8'))
            else:
                client.send("Sorry, wrong answer\n".encode('utf-8'))

        

if __name__ == "__main__":
    main()
    