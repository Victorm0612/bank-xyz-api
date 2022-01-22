# bank-xyz-api

This is the BackEnd of xyz-bank project of the WWW course at Universidad del Valle.

# Setup

To run the Django project it is necessary to do it from a Linux distribution, if you are a Windows user, the recommendation is to use **WSL**.

- [guide](https://docs.microsoft.com/en-us/windows/wsl/install-manual)

After you have WSL on your computer, install en vscode an extension called **Remote - WSL**. Then run a new WSL Window and open a terminal.

Now it is necessary to install python, therefore, execute the following line:
`sudo apt update && upgrade sudo apt install python3 python3-pip ipython3`

Now you can install Django:
`python3 -m pip install Django`

To run server execute:
`python3 manage.py runserver`
