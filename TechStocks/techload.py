import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import json
import sys

connection = sqlite3.connect("tech.db")
cur = connection.cursor()

startdate_str = ''
enddate_str = ''
startdate = ''
enddate = ''

cur.execute("SELECT * FROM Stocks ORDER BY ROWID ASC LIMIT 1")
firstdate = datetime.strptime(cur.fetchone()[1],"%m/%d/%Y")
cur.execute("SELECT * FROM Stocks ORDER BY ROWID DESC LIMIT 1")
lastdate = datetime.strptime(cur.fetchone()[1],"%m/%d/%Y")

while True:
    startdate_str = input('Please enter a start date - ')
    if (startdate_str == 'quit'):
        quit()
    enddate_str = input('Please enter an end date - ')
    if (enddate_str == 'quit'):
        quit()

    startdate = datetime.strptime(startdate_str,"%m/%d/%Y")
    enddate = datetime.strptime(enddate_str,"%m/%d/%Y")

    if(startdate < firstdate):
        print("Please enter valid start date after",firstdate)
        print("Type quit to exit the program")
        continue

    if(enddate > lastdate):
        print("Please enter a valud end date before",lastdate)
        print("Type quit to exit the program")
        continue

    if(enddate < startdate):
        print("Please enter valid start and end dates")
        print("Type quit to exit the program")
        continue
    if(startdate <= enddate):
        break

dic = {}

dic["Apple"] = []
dic["Google"] = []
dic["Msft"] = []

dates = []

for row in cur.execute("SELECT * FROM Stocks"):
    date = datetime.strptime(row[1],"%m/%d/%Y")
    if(date >= startdate and date <= enddate):
        dates.append(date)
        dic["Apple"].append(row[2])
        dic["Google"].append(row[3])
        dic["Msft"].append(row[4])

cur.close()

# to make this code generalized for any amount of stock data to be entered, simply use something
# like a dictionary that maps the stock name to a list of its prices over time. Or use a pandas
# dataframe instead of a database as that is much easier. Only using database for this assignment.
# Then simply map the dates with each one of the list of prices with the stock name then name the saved fig
# as the stock name then use the stock name on the visualization when I rank the stock performances and
# color it red or green depending on if it went up or down. This method will ensure I always keep a
# way to access the stock name and its prices over time and loop through them if needed.

percents = {}

for key in dic:
    percent = 0
    try:
        percent = int((dic[key][-1] - dic[key][0])/dic[key][0] * 100)
    except:
        print("The dates you submitted had no trading days between them.")
        quit()

    percents[key] = percent

    plt.plot_date(dates,dic[key],linestyle='solid')
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%m/%d/%y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.tight_layout()
    plt.title(key + ' Stock Price')
    plt.xlabel('Date (Month/Day/Year)')
    plt.ylabel('Closing Price')
    plt.savefig("Visualization/charts/"+key+".png",bbox_inches="tight",transparent=True)
    plt.cla()

order = sorted(percents.items(), reverse=True, key=lambda item:item[1])

sys.stdout = open("Visualization/finaldata.js",'w')
jsonobj = json.dumps(order)

print("var jsonstr = '{}' ".format(jsonobj))

