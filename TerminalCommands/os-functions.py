import os
import datetime

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,'w') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))



def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.exists(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,'x') as file:
    pass

  # Return the list of files in the new directory
  os.chdir('..')
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

def file_date(filename):
  # Create the file in the current directory
  with open(filename,'x') as file:
    pass
  timestamp = os.path.getmtime(filename)
  timestamp = datetime.datetime.fromtimestamp(timestamp)
  string = str(timestamp)
  # Convert the timestamp into a readable format, then into a string
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(string[:10]))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

def parent_directory():
  # Create a relative path to the parent
  # of the current working directory

  os.chdir('..')

  # Return the absolute path of the parent directory
  return os.getcwd()

print(parent_directory())