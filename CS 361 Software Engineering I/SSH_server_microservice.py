# CS 361 Microservice
# Simple program to receive a request and read the user's 
# SSH config file and current hosts in that file.  Once the
# file has been read this program will send back an object
# of all hosts in the SSH config file

from paramiko import SSHConfig
import zmq
import zmq.utils.win32
from time import sleep


print("***THIS IS THE SSH MICROSERVICE***")

# Setting up PyZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def stop_my_application():
    print("W: interrupt received, stopping...")
    socket.close()
    context.term()


def main():
# Loop to handle requests and responses
    while True:

        # zmq.utils.win32.allow_interrupt allows user to send 
        # CTRL-C to microservice to stop the process
        with zmq.utils.win32.allow_interrupt(stop_my_application):
            message =  socket.recv_multipart()
        print("Received request: %s" % message)
        ssh_message = message[0].decode("utf-8")
        username = message[1].decode("utf-8")
        operating_sys = message[2].decode("utf-8")

        if ssh_message == "send_sshconfig":
            if operating_sys == "Windows":
                ssh_config = SSHConfig.from_path("C:\\Users\\" + username + "\\.ssh\\config")
            else:
                ssh_config = SSHConfig.from_path("/home/" + username + "./ssh/config")
            print("Sending ssh_config object")
            sleep(0.25)
            print("End of data transmission\n")
            socket.send_pyobj(ssh_config)
        else:
            ssh_config = "not_available"
            socket.send_string(ssh_config)


if __name__ == "__main__":
    main()