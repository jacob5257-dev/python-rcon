import os
from mcrcon import MCRcon

os.system("cls")
ip = input("Enter server ip (ipv4 format): ")
os.system("cls")
password = input("Enter server password: ")
os.system("cls")

while True:
    command = input("Enter command you want to execute: /")
    with MCRcon(ip, password) as mcr:
        resp = mcr.command(command)
        print(resp)