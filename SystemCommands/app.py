
# We run these system/terminal commands with the subprocess module in python which makes it so
# like you are calling the commands straight on the terminal. This is great because you are
# essentially running system commands in a python program.

import subprocess

result = subprocess.run(['date'],capture_output=True)
print(result.stdout.decode())

result = subprocess.run(['ls','/Users/malamapono/Desktop/folder'],capture_output=True)
print(result.stdout.decode())




