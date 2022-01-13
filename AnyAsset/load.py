import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import json
import sys
import os
import glob

# removing all previous charts
files = glob.glob('/Users/malamapono/PyCharmProjects/AnyAsset/Visualization/charts/*')
for f in files:
    os.remove(f)

def remove(list):
    # remove first and last things
    list.pop(0);
    list.pop(-1);
    return list

# filename = input("Enter a file - ")
filename = 'manystocks.csv'

df = pd.read_csv(filename)

column_names = df.columns.tolist()
# column_names = remove(df.columns.tolist())
# use this remove method if there are certain extra columns that you need to clear in order to
# clean up your data and only get the info you want. You can also make a method to remove extra rows
# to again clean the data.

assets = {}

for name in column_names:
    column = df[name].tolist()
    assets[name] = column

startdate_str = ''
enddate_str = ''
startdate = ''
enddate = ''

firstdate = datetime.strptime(assets['Date'][0],"%m/%d/%Y")
lastdate = datetime.strptime(assets['Date'][-1],"%m/%d/%Y")

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

startIndex = None
endIndex = None

dates = assets['Date']
assets.pop('Date')

index = 0
for date in dates:
    real_date = datetime.strptime(date,"%m/%d/%Y")
    if(real_date == startdate):
        startIndex = dates.index(date)
    if(real_date == enddate):
        endIndex = dates.index(date)
    dates[index] = real_date
    index+=1

if(startIndex == None or endIndex == None):
    print("The dates you submitted had no trading days between them. Please try again.")
    quit()

dates = dates[startIndex:endIndex+1]

for key in assets:
    assets[key] = assets[key][startIndex:endIndex+1]

for key in assets:
    plt.plot_date(dates,assets[key],linestyle='solid')
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%m/%d/%y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.tight_layout()
    plt.title(key + ' Price')
    plt.xlabel('Date (Month/Day/Year)')
    plt.ylabel('Closing Price')
    plt.savefig("Visualization/charts/"+key+".png",bbox_inches="tight",transparent=True)
    plt.cla()

for key in assets:
    values = assets[key]
    percent = int((values[-1] - values[0]) / values[0] * 100)

    assets[key] = percent

order = sorted(assets.items(), reverse=True, key=lambda item:item[1])
# list of tuples. Each tuple has a asset name and its percent change over the time entered. The list is sorted.

sys.stdout = open("Visualization/finaldata.js",'w')
jsonobj = json.dumps(order)

print("var jsonstr = '{}' ".format(jsonobj))