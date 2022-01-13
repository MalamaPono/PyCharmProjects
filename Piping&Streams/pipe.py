
#  THE SHEER POWER OF PIPING IS EXTRAORDINARY
# Use sys.stdin to read lines of a file and capitalize the first letter of each line than write that
# out to a new file or just print it in the terminal.

# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     print(line.capitalize())

# cat poem.txt | python3 pipe.py    to print on the terminal
# cat poem.txt | python3 pipe.py > capitalized.txt      to write to new file capitalized.txt



# Pipe some text from a file and split each word, then count up the occurances of each word,
# then print out the top 10 most common words in order.
# cat new.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head


# Sort some piece of text write it into an intermediary python file that will print the lines, then
# write that into a new file.
# sort poem.txt | python3 pipe.py > newfile.txt


# QWIKLABS FINAL ASSIGNMENT IDENTIFYING AND RENAMING FILES WITH PYTHON SCRIPTS AND SYSTEM COMMANDS

import sys
import subprocess
import os
# identify the old files in the directory that need to be changed and write their names to a new file
# called oldFiles.txt
def identifyOldFiles():
    grep = subprocess.run(['grep',' jane ','list.txt'],capture_output=True)
    entries = [line for line in grep.stdout.decode().split("\n") if line!=""]
    filename_only = [line.split()[2][1:] for line in entries]

    with open('oldFiles.txt','w') as oldFiles:
        for filename in filename_only:
            if os.path.exists(filename):
                oldFiles.write(filename + "\n")

# rename the files in the directory
def renameOldFiles(argv):
    oldFiles = argv[1]
    with open(oldFiles) as file:
        for old_name in file:
            old_name = old_name.strip()
            new_name = old_name.replace('jane','jdoe')
            subprocess.run(['mv',old_name,new_name])
    file.close()

def main():
    identifyOldFiles()
    renameOldFiles(sys.argv)

main()