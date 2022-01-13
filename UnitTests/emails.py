
# FINAL QWIKLABS ASSIGNMENT FOR TESTING AND EXCEPTIONS

# Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts, called
# emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works
# great — you enter in an employee's name and their email is printed to the screen. But, for some employees, the
# output doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and
# verify that all the tests pass to make sure the script works! Best of luck!
#
# What you'll do
# In this lab, you will:
#
# Write a simple test to check for basic functionality
# Write a test to check for edge cases
# Correct code with a try/except statement'

import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  fullname = ""
  try:
    fullname = str(argv[1] + " " + argv[2])
  except IndexError:
    return 'Missing Parameters'
  # Preprocess the data
  filename = '/home/student-03-e015e072e4d3/data/user_emails.csv'
  filename = 'user_emails.csv'
  email_dict = populate_dictionary(filename)
  # Find and print the email
  return email_dict.get(fullname.lower(),'No email address found')

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()
