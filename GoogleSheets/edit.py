# uses packages from pypi installed through pip which makes code more easy to use
# and has a lot more functionalities that are built and made for the user to have more
# power to do what they want.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scope)

client = gspread.authorize(creds)

sheet = client.open("Sports").sheet1
data = sheet.get_all_records()
# pprint(data)

def findAverage(col):
    totalSum = 0;
    for row in range(2,len(data) + 2):
        cellVal = sheet.cell(row,col).value
        if not cellVal == None:
           totalSum += int(cellVal)

    return totalSum/len(data)

def decrementCredits(name,amount):
    cell = sheet.find(name)
    row = sheet.row_values(cell.row)
    print(row)

    creditCellValue = int(sheet.cell(cell.row,2).value) - amount

    if creditCellValue == 0:
        print(f"{cell.value} ran out of credits and is now at 0")
        print("Please buy more credits")

    strRepresentation = str(creditCellValue)

    sheet.update_cell(cell.row,2,strRepresentation)

# decrementCredits("Johanna Smith",5)

# helpful lines
# data = sheet.get_all_records()
# row = sheet.row_values(3)
# col = sheet.col_values(3)
# cell = sheet.cell(2,1).value
# insertRow = [94,0,"NEW DATA","Knitting"]
# sheet.insert_row(insertRow,4)
# sheet.delete_rows(4)
# numRows = sheet.row_count
# numCols = sheet.col_count

# cell_list = sheet.findall("Honolulu")
# for cell in cell_list:
#     sheet.update_cell(cell.row, cell.col, "CHANGED")


print(findAverage(4))