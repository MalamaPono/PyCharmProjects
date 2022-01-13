import os
import csv

# We're working with a list of flowers and some information about each one. The create_file function writes this
# information to a CSV file. The contents_of_file function reads this file into records and returns the information in
# a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a
# dictionary using DictReader.
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


#  Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without
#  turning it into a dictionary. How do you skip over the header record with the field names?
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  with open(filename,'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


# Parsing the employees.csv file
def read_employees(csvfile_location):
  employee_list = []
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csvfile_location), dialect='empDialect')
  for row in employee_file:
    employee_list.append(row)
  return employee_list

employee_list = read_employees('employees.csv')

def process_data(dics):
  department_list = []
  for dic in dics:
    department_list.append(dic['Department'])

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

dictionary = process_data(employee_list)

def write_report(dic,report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

write_report(dictionary, 'result.txt')


# FINAL QWIKLABS ASSIGNMENT. PARSE A CSV FILE ABOUT EMPLOYEES AND FORM A GIVEN START DATE
# TO PRESENT, LIST ALL THE PEOPLE WHI HAVE STARTED WORKING SINCE THEN, AND THEIR SPECIFIC
# START DATE.

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
  """Interactively get the start date to query for."""

  print('Getting the first start date to query for.' + "\n")
  print('The date must be greater than Jan 1st, 2018')
  year = int(input('Enter a value for the year: '))
  print("\n")
  month = int(input('Enter a value for the month: '))
  print("\n")
  day = int(input('Enter a value for the day: '))
  print("\n")

  return datetime.datetime(year, month, day)


def get_file_lines(url):
  dic = {}
  # Download the file over the internet
  response = requests.get(url, stream=True)
  lines = []

  for line in response.iter_lines():
    lines.append(line.decode("UTF-8"))

  csv_data = csv.reader(lines[1:])
  for l in csv_data:
    str_date = l[3]
    real_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    lis = dic.get(real_date, [])
    lis.append(l[0])
    dic[real_date] = lis

  return dic


def get_same_or_newer(start_date, dic):
  if start_date in dic:
    return dic[start_date]
  else:
    return None


def list_newer(start_date, dic):
  while start_date < datetime.datetime.today():
    employees = get_same_or_newer(start_date, dic)
    if employees:
      for employee in employees:
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employee))

    # Now move the date to the next one
    start_date = start_date + datetime.timedelta(days=1)


def main():
  start_date = get_start_date()
  dic = get_file_lines(FILE_URL)
  list_newer(start_date, dic)


if __name__ == "__main__":
  main()