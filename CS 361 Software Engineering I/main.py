# Daniel Reid Nelsen
# CS 361
# Porfolio Project
# Description:  This project is a simple program to demonstrate
#               Agile software engineering principles and software
#               design.  This project incorporates Inclusivity 
#               Heuristics.

from paramiko import SSHConfig
from subprocess import Popen
from os import getlogin
from sys import exit
from time import sleep
from platform import system
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def main_screen():
    """
    Main screen for opening SSH Sessions
    """

    close_program = False

    while close_program == False:
        print("      ****Stored SSH Hosts****")

        ssh_config = get_sshconfig_from_microservice()
        hostnames = sorted(list(ssh_config.get_hostnames()))

        print_hosts(hostnames)
        option = print_options()

        match option:
            case "1":
                open_host(ssh_config, hostnames)
            case "2":
                add_ssh_host()
            case "3":
                help_screen()
            case "4":
                close_program = exit_screen()
            case _:
                print("Please choose one of the options.\n")


def print_hosts(hostnames):
    """ 
    Prints Host names to screen from SSH Config file
    """

    print("\nCurrent SSH Hosts:")
    for num, val in enumerate(hostnames):
        if val != "*":
            print(num, val)


def open_host(ssh_config, hostnames):
    """
    Open SSH Host
    """

    print("Which host would you like to connect to?")
    print("Input number")
    host_number = input("\n>:")
    ssh_config.lookup(hostnames[int(host_number)])
    open_ssh_host(hostnames[int(host_number)])


def add_ssh_host():
    """
    Edit/Add/Delete SSH Host from config file
    """
    print("From this screen Add an SSH Host")

    close_program = False

    while close_program == False:

        option = print_add_menu()

        match option:
            case "1":
                add_host_menu()
            case "2":
                return
            case "3":
                add_ssh_help_menu()
            case "4":
                exit_screen()
            case _:
                print("Please choose one of the options.\n")

    return


def add_host_menu():
    """
    Menu to add SSH Host to config file.
    """

    ssh_options = []

    print("Adding SSH Host information...\n")
    ssh_options.append(input("Please enter name of host: "))
    ssh_options.append(input("Enter IP address of Host: "))
    ssh_options.append(input("Enter login name for host: "))
    ssh_options.append(input("Enter location and name of private SSH key: "))

    if confirm_write_config(ssh_options):
        add_ssh_to_file(ssh_options)
        print("Writing new host to SSH config file")
        sleep(0.25)
        print("New SSH Host added!")
    else:
        print("Host NOT added")

    return


def confirm_write_config(ssh_options):
    """
    Confirm writing SSH host to config file.

    Return: True for writing host
            False to not write the host
    """

    print("\nConfirm writing new host to SSH config file.")
    print("Are these values correct?\n")

    print("Host Name    = ", ssh_options[0])
    print("IP Address   = ", ssh_options[1])
    print("Username     = ", ssh_options[2])
    print("Key location = ", ssh_options[3], "\n")

    print("Y - write information to SSH config file")
    print("N - Do NOT write information.")
    confirm = input("\n>: ")

    if confirm == "Y" or confirm == "y":
        return True

    return False


def add_ssh_to_file(ssh_options):
    """
    Adds SSH information to SSH config file
    """

    ssh_path = locate_ssh_config()

    with open(ssh_path, "a") as file:
        file.write("\n\n")
        file.write("Host " + ssh_options[0] + "\n")
        file.write("\tHostname " + ssh_options[1] + "\n")
        file.write("\tUser " + ssh_options[2] + "\n")
        file.write("\tIdentityFile " + ssh_options[3])


def locate_ssh_config():
    """
    Locate ssh config file based on operating system
    """

    operating_system = get_os()
    username = get_username()

    if operating_system == "Windows":
        ssh_config = "C:\\Users\\" + username + "\\.ssh\\config"
    else:
        ssh_config = "/home/" + username + "./ssh/config"

    return ssh_config


def add_ssh_help_menu():
    """
    Help file for adding SSH Host
    """

    help = True

    while help == True:
        print("SSH Organizer Documentation\n")
        print("From the options below select a number to get see")
        print("more information about that feature\n")
        print("1 - Add SSH Host")
        print("2 - Exit Help Screen")
        option = input("\n>: ")

        if option == "1":
            print("\n              ***Add SSH Host***")
            print("This option will allow you to add an SSH host to the ")
            print("SSH Config file.  You will need to know the IP address")
            print("and location of the SSH key file. If this ")
            print("information is missing then the SSH Host may not")
            print("work as intended.")
            print("              **********************\n\n")
        else:
            help = False


def print_add_menu():
    """
    Prints Menu for adding SSH Host
    """

    print("\nSelect Option Below:")
    print("1. Open menu to add SSH Host")
    print("2. Return to SSH menu")
    print("3. Go to help menu")
    print("4. Quit Program")

    option = input("\n>: ")

    return option


def get_sshconfig_from_microservice():
    """
    Function to get ssh config object from microservice
    """

    print("Sending message to SSH Config Microservice")
    message = "send_sshconfig"
    socket.send_string(message, flags=zmq.SNDMORE)
    socket.send_string(get_username(), flags=zmq.SNDMORE)
    socket.send_string(get_os())
    sleep(0.25)

    try:
        sshconfig = socket.recv_pyobj()
    except:
        sshconfig = ""

    return sshconfig


def print_options():
    """
    Prints options for Stored SSH screen
    """

    print("\nSelect Option Below:")
    print("1. Open SSH Session")
    print("2. Add SSH Host")
    print("3. Open Help Information Screen")
    print("4. Quit Program")

    option = input("\n>: ")

    return option


def get_username():
    """
    Returns username
    """

    username = getlogin()

    return username


def get_os():
    """
    Returns current operating system
    """

    return system()


def exit_screen():
    """
    Screen to confirm exiting the program
    """

    print("\nAre you certain that you want to exit the program?")
    print("1. Confirm Exit")
    print("2. Cancel Exit")
    option = input("\n>: ")

    if option == "1":
        print("\nHave a great day!\n")
        exit()
    else:
        return False


def open_ssh_host(host):
    """
    Opens terminal with SSH session
    """

    terminal = "wezterm.exe start -- ssh " + host
    open_terminal = terminal.split()
    print("\nOpening SSH session to: ", host, "\n")
    Popen(open_terminal)
    sleep(1)


def help_screen():
    """
    Interactive Help screen for Stored SSH Hosts Screen
    """

    help = True

    while help == True:
        print("SSH Organizer Documentation\n")
        print("From the options below select a number to get see")
        print("more information about that feature\n")
        print("1 - Open SSH Session")
        print("2 - Exit Help Screen")
        option = input("\n>: ")

        if option == "1":
            print("\n              ***Open SSH Session***")
            print("This option will open a terminal and start an SSH session")
            print("with the selected host")
            print("              **********************\n\n")
        else:
            help = False


def main():
    """
    Starting Screen - Explains program to user.
    """

    close_program = False

    mystring = """
    .d8888. .d8888. db   db       .d88b.  d8888b.  d888b   .d8b.  d8b   db d888888b d88888D d88888b d8888b. 
    88'  YP 88'  YP 88   88      .8P  Y8. 88  `8D 88' Y8b d8' `8b 888o  88   `88'   YP  d8' 88'     88  `8D 
    `8bo.   `8bo.   88ooo88      88    88 88oobY' 88      88ooo88 88V8o 88    88       d8'  88ooooo 88oobY' 
      `Y8b.   `Y8b. 88~~~88      88    88 88`8b   88  ooo 88~~~88 88 V8o88    88      d8'   88~~~~~ 88`8b   
    db   8D db   8D 88   88      `8b  d8' 88 `88. 88. ~8~ 88   88 88  V888   .88.    d8' db 88.     88 `88. 
    `8888Y' `8888Y' YP   YP       `Y88P'  88   YD  Y888P  YP   YP VP   V8P Y888888P d88888P Y88888P 88   YD 
    """
    print(mystring)

    while close_program == False:

        print("Welcome to the SSH Organizer!")
        print("This program will allow you to save your remote SSH Hosts.")
        print("\nThe SSH Organizer can also open your terminal of choice.")
        print("\nInteraction with this program is through the command prompt.")
        print("Push enter after you input an option.")
        print("\nPlease select on of the options to continue:")
        print("1. Continue to Main SSH Screen")
        print("2. Quit")
        option = input("\n>: ")

        if option == "1":
            main_screen()

        elif option == "2":
            close_program = exit_screen()


if __name__ == "__main__":
    main()
