import subprocess

with open('output.txt','w') as file:
    p1 = subprocess.run('ls',capture_output=True)
    file.write(p1.stdout.decode())