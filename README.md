# Python RCON File
This repository holds a python file that you can use on your Minecraft server.

## Prerequisites
You must have both a functioning Minecraft server and the [latest version of Python](https://www.python.org/downloads/) installed.  Your OS does not matter as long you have the two things listed above.

## Setup
1. You must first fully start a Minecraft server. It does not matter if you use a vanilla server or a fork (Bukkit, Spigot, Paper, etc). The setup instructions are the same.
2. Download the `rcon.py` file.
3. Locate the following lines in your `server.properties` file:
```
rcon.port=25575
enable-rcon=false
rcon.password=
```
Do **NOT** change the first line. Change the second line to `enable-rcon=true` and the third to `rcon.password=yourPassword`. Remember your password as it will be used later. If neccessary [port forward](https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/) port **25575**.
3. Save the file and execute `/reload` in your server console to reload the configuration file.
4. Open your terminal and execute `pip install mcrcon`.
5. Run the python file.

## Wanna contribute?
Create a pull request or sumbit an issue. The team will review your suggestion and make the neccessary changes.

## License
This repository and all files inside of it are licensed under the MIT license. Feel free to use this as a base for any program you choose. The "mcrcon" package is not mine and full credit for the package goes to Adrian Turjak. The package can be found on PyPi [here](https://pypi.org/project/mcrcon/).
