import calendar
import datetime
from bs4 import BeautifulSoup
from requests import get
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# basically this takes in a month and year and gets the time and date of all submissions from that month
# kind of slow but what can you do. look into fixing
# new: added matplotlib plotting instead of exporting csv and plotting in R like a caveman
            
def date_iter(year, month):
    for i in range(1, calendar.monthlen(year, month) + 1):
        yield datetime.date(year, month, i)
    
def getDateList(month, year=2021):
    #returns list of strings of all dates in month
    dateList = []
    for d in date_iter(year, month):
        dateList.append(str(d))
    return dateList

def submTimes(date_str):
    L = []
    url_str = "https://dad.gallery/submissions?date="+date_str
    response = get(url_str)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for sub in html_soup.find_all('div', class_='submissionNotes'):
        timestamp = (''.join(sub.next_element))
        L.append(timestamp.strip())
    return L

    
def writecsv(path, L):
    with open(path,'w', newline='') as csvfile:
        myWriter = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
        myWriter.writerow("T")
        #myWriter.writerow(timeList)
        for item in L:
            myWriter.writerow([item])
        #myWriter.writerows(iter(timeList))

def getFull(month):
    days = getDateList(month)
    full = []
    for d in days:
        t = submTimes(d)
        for time in t:
            full.append(d + ' ' + time)
    print("done!")
    return full

allDateTimes = getFull(4) #April
#allDates = [x.split()[0] for x in allDateTimes] #well this isn't as interesting information honestly
#maybe a function to get all times for a specific date
#allTimes = [x.split()[1] for x in allDateTimes]
writecsv("temp.csv", allDateTimes)

#TODO: figure out how to histogram time series (just the time no date) in matplotlib why is this difficult
'''
tmp = ["23:59:59", "23:59:00", "23:30:00", "20:00:00", "00:00:01", "01:00:00", "12:30:00", "14:20:10", "12:34:56"]
a = [datetime.datetime.strptime(x, "%H:%M:%S").time() for x in tmp]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8]
'''