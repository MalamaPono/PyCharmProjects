# this read.py file uses functionalities to read and change values in google sheets
# straight from the google API code and service account so it is not really user friendly.
# It is kind of confusing and doesn't have many functions, so it is easier to use
# already built in packages from pypi which we can install through the help of pip.
# These packages are built by coders like me so it is easier to understand and has a lot
# more functions to help with daily tasks and automations we would want to use.

from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Pvrdmzo9AD6CIYyEjvmlJnyTYsMnURTEN6vQ0sxMzs8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API then read all the values in the sheet
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:D30").execute()
values = result.get('values', [])
print(values)

# add new data with specific column information into a new sheet
addition = [["Gamestop",5000],["Sofi",10000],["Tesla",20000]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet2!A1", valueInputOption="USER_ENTERED", body={"values":addition}).execute()