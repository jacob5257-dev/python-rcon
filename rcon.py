import os
from mcrcon import MCRcon

os.system("cls")
ip = input("Enter server ip (ipv4 format): ")
os.system("cls")
password = input("Enter server password: ")
os.system("cls")

while True:
    try:
        command = input("Enter command you want to execute: /")
        with MCRcon(ip, password) as mcr:
            resp = mcr.command(command)
            print(resp)
    except ImportError:
        print("There was an error running your command. Try installing pip and all neccesary packages and try again. For help please refer to https://github.com/jacob5257-dev/python-rcon")
        temp = input("Press enter to continue...")
        break
    except:
        print("There was an unexpected error running your command. Check your server ip (" + ip + ") and your server password (" + password + ") are correct and try again. If you believe this message to be in error, submit an issue at https://github.com/jacob5257-dev/python-rcon")
        temp = input("Press enter to continue...")
        break
