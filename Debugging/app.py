# Steps to debug any technical problem
# 1. Gather information
# 2. Try and reproduce the error and find the error case
# 3. Make sure the problem doesn't happen again by first providing short term solutions, but
# in the longer run finding a longer term solution that is sustainable.


# The compare_strings function is supposed to compare just the alphanumeric content of two strings, ignoring upper vs
# lower case and punctuation. But something is not working. Fill in the code to try to find the problems, then fix the
# problems.

import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = "[.?!,;:-']"
  for punc in punctuation:
      if punc in string1:
        string1 = string1.replace(punc,"")
      if punc in string2:
        string2 = string2.replace(punc, "")

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False


# The datetime module supplies classes for manipulating dates and times, and contains many types, objects, and methods.
# You've seen some of them used in the dow function, which returns the day of the week for a specific date. We'll use
# them again in the next_date function, which takes the date_string parameter in the format of "year-month-day", and
# uses the add_year function to calculate the next year that this date will occur (it's 4 years later for the 29th of

# February during Leap Year, and 1 year later for all other dates). Then it returns the value in the same format as it
# receives the date: "year-month-day".
#
# Can you find the error in the code? Is it in the next_date function or the add_year function? How can you determine
# if the add_year function returns what it's supposed to? Add debug lines as necessary to find the problems, then fix
# the code to work as indicated above.
#

import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails,
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string,
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29


# The best_search function compares linear_search and binary_search functions, to locate a key in the list, and returns
# how many steps each method took, and which one is the best for that situation. The list does not need to be sorted,
# as the binary_search function sorts it before proceeding (and uses one step to do so). Here, linear_search and binary
# _search functions both return the number of steps that it took tomvhb either locate the key, or determine that it's not
# in the list. If the number of steps is the same for both methods (including the extra step for sorting in
# binary_search), then the result is a tie. Fill in the blanks to make this work.

def linear_search(list, key):
  # Returns the number of steps to determine if key is in the list

  # Initialize the counter of steps
  steps = 0
  for i, item in enumerate(list):
    steps += 1
    if item == key:
      break
  return steps


def binary_search(list, key):
  # Returns the number of steps to determine if key is in the list

  # List must be sorted:
  list.sort()

  # The Sort was 1 step, so initialize the counter of steps to 1
  steps = 1

  left = 0
  right = len(list) - 1
  while left <= right:
    steps += 1
    middle = (left + right) // 2

    if list[middle] == key:
      break
    if list[middle] > key:
      right = middle - 1
    if list[middle] < key:
      left = middle + 1
  return steps


def best_search(list, key):
  steps_linear = binary_search(list,key)
  steps_binary = binary_search(list,key)
  results = "Linear: " + str(steps_linear) + " steps, "
  results += "Binary: " + str(steps_binary) + " steps. "
  if (steps_linear < steps_binary):
    results += "Best Search is Linear."
  elif (steps_binary < steps_linear):
    results += "Best Search is Binary."
  else:
    results += "Result is a Tie."

  return results


print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
# Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
# Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
# Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
# Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
# Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.