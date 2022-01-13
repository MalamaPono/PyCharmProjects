import re
#
#
# BASIC REGULAR EXPRESSIONS TEST
#
#
# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains
# alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign,
# followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular
# expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters,
# and character classes.
def check_web_address(text):
  pattern = r'^(\w+|[\.\-+])+\.[a-zA-Z]+$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with
# no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in
# upper or lower case. Fill in the regular expression to do that.
def check_time(text):
  pattern = r"^(1[012]|[0-9]):[0-5][0-9] ?(am|pm|PM|AM)$"
  # digits can only be [0-9] cannot do like [1-12] to stand for numbers 1,2,3,4,5,6,7,8,9,10,11,12
  # it can only be a valid range of single characters like digits 0-9 or letters a-z
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#
# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by
# parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is
# met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for
# text-based communication" should return True since (IM) satisfies the match conditions."
def contains_acronym(text):
  pattern = r'\([A-Z]|[0-9][a-zA-Z0-9]+\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5
# digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at
# least one space, and cannot be at the start of the text.
def check_zip_code (text):
  result = re.search(r" +\d{5}\-?\d?\d?\d?\d?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


def rearrange_name(name):
  result = re.search(r"^(\w*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

# Extracts Person's id from a login line.
def extract_pid(log_line):
    pattern = r"\[(\d+)\]"
    result = re.search(pattern,log_line)
    if result is None:
        return ""
    else:
        return result[1]

# NOTES:

# NEVER USE PARENTHESIS TO GROUP SOMETHING FOR A CERTAIN OPERATION LIKE * OR + OR ?, RATHER
# APPLY * OR + OR ? TO EACH CHARACTER IN THAT GROUP YOU WOULD HAVE PUT PARENTHESIS AROUND.
# PARENTHESIS SPECIFY CAPTURE GROUPS, NOT WHAT YOU WANT TO DO FOR GROUPING KOCHA.

# characters that need to be escaped with \ if you actually want to use them
# \\ means that you are escaping the backslash meaning it will match a \
#  [] () ? * . ^ $ | \

# useful other regex methods
# 1. .split() method which is similar to split() method for strings, but adds the ability to split
# based on regular expression matching instead of just a regular string
# 2. .sub() method is similar to the string replace method but adds the ability to use regular expressions
# for both the matching and replacing instead of both regular strings. Replacing parameter
# usually is a normal string, but can be a regular expression that maybe switches something like
# alters the capturing groups in the matching section. All instances of the regular expression that
# is matched will be replaced with your replacement regular expression/regular string.

# import re
# original = '123 ghb 564 bhn 679 dfd'
# changed = re.sub(r'(\d+) ([a-z]+)',r'\2 \1', original)
# print(changed)


# DIFFICULT REGULAR EXPRESSIONS TEST


# We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone
# number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the
# international format, with "+1-" in front of the phone number.
def transform_record(record):

  pattern = r'(\d{3}\-?\d{3}\-?\d{4})'
  new = r'+1-\1'

  new_record = re.sub(pattern,new,record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer


# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u).
def multi_vowel_words(text):
  pattern = r'\b[a-zA-Z]*?[aeiouAEIOU]{3,}[a-zA-Z]*\b'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []


# The transform_comments function converts comments in a Python script into those usable by a C compiler. This means
# looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C singleline
# comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a
# Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks
# (##), (###), etc., # as a single comment indicator, to be replaced with just (//) and not (#//) or (//#).
def transform_comments(line_of_code):
  pattern = r'(.*?)#+(.+)'
  new = r'\1//\2'
  result = re.sub(pattern,new,line_of_code)
  return result

print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"


# The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3
# more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this:
# (XXX) XXX-XXXX. Fill in the regular expression to complete this function.
def convert_phone_number(phone):
  # grouping each set of numbers
  pattern = r'\b(\d{3})\-(\d{3})\-(\d{4})\b'
  new = r'(\1) \2-\3'
  result = re.sub(pattern,new,phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



# We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets.
# We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to
# extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
def show_time_of_pid(line):
  pattern = '^(\w{3} \d \d{2}:\d{2}:\d{2}).+\[(\d+)\].+'
  result = re.search(pattern, line)
  return f'{result[1]} pid:{result[2]}'

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440




# REGEX FINAL QWIKLABS ASSIGNMENT 1:

import csv
import re

def contains_domain(address, domain):
  pattern = r'.+@(.+)$'
  result = re.search(pattern,address)
  return result[1] == domain
# Returns True if the email address contains the given domain,
# in the domain position, false if not.

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in
    the received address."""
  new_address = address
  if contains_domain(address,old_domain):
    new_address = re.sub(old_domain,new_domain,address)
  return new_address

def main():
  old_domain,new_domain = 'abc.edu','xyz.edu'
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  csv_file_location = 'user_emails.csv'
  # csv_file_location = '/home/student-03-e015e072e4d3/data/user_emails.csv'
  # report_file = '/home/student-03-e015e072e4d3/data/updated_user_emails.csv'
  report_file = 'updated_user_emails.csv'

  user_data_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open('user_emails.csv') as file:
    reader = csv.reader(file)
    user_data_list = list(reader)
    user_email_list = [user[1].strip() for user in user_data_list[1:]]

    for email in user_email_list:
      if contains_domain(email,old_domain):
        old_domain_email_list.append(email)
        new_email = replace_domain(email,old_domain,new_domain)
        new_domain_email_list.append(new_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
    file.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()


# REGEX FINAL QWIKLABS ASSIGNMENT 2 WORKING WITH LOG FILES:

# Imagine one of your colleagues is struggling with a program that keeps throwing an error. Unfortunately, the program's
# source code is too complicated to easily find the error there. The good news is that the program outputs a log file
# you can read! Let's write a script to search the log file for the exact error, then output that error into a separate
# file so you can work out what's wrong.
#
# What you'll do
# Write a script to search the log file using regex to find for the exact error.
# Report the error into a separate file so you know what's wrong for further analysis.

import os
import re
import sys

def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []

  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

    if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
      returned_errors.append(log)
    file.close()
  return returned_errors

  # return the list of logs that had errors in them.

def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log','w') as file:
    for errorlog in returned_errors:
      file.write(errorlog)

if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

