# This is the official copy for grading picks
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets
import pandas as pd

# The ID and range of a sample spreadsheet.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_2019_5pick.json', scope)
gc = gspread.authorize(credentials)
gc1 = pygsheets.authorize(service_file='client_secret_2019_5pick.json')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
wks = gc.open_by_key('1xxxx')
sheet = wks.worksheet("Week 1")

sh = gc1.open_by_key('xxxxxx')
#wks1 = sh[17]
wks1 = sh.worksheet('title', 'Week 1')



# create dictionary for the spread from list of lists(excel sheet)
# grab all data into list of lists, using gspread to read data
ExcelSheetSecondRead = sheet.get_all_values()


spread = {}

for i in ExcelSheetSecondRead[1:]:
    if i[9] != "" and i[10] != "":
        spread[i[9]] = float(i[10])
print(spread)


# build players pick list
picks = []
# build the Players picks list
for row in ExcelSheetSecondRead[1:]:
    # picks[row[1], row[2], row[3], row[4]]
    picks.append(row[0:7])
print(picks)

# Step 3 grade: compare spread{} to picks[] and write out # in picks list
d2 = pd.DataFrame()
for p in picks:
    score = float(p[6])
    score += float(spread[p[1]])
    score += float(spread[p[2]])
    score += float(spread[p[3]])
    score += float(spread[p[4]])
    score += float(spread[p[5]])
    p[6] = score
print(picks)

d2 = picks
wks1.update_values((2, 1), d2)
