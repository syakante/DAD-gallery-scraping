import re

from lxml import html 
import requests
'''
def read(path):
    with open(path,"rt") as f:
        return f.read()
'''
def writeSpace(dlim="\n"):
    #writes the txt file, optional parameter for whether to divide with newline, space, comma, etc
    with open("dad-active-users.txt", "wt", encoding="utf-8") as f:
        for user in userList:
            f.write(user+dlim)
            
#webscrape the html page as text
allTxt = requests.get('https://dad.gallery/challenges/1').text
#find the table containing users with a streak
tableCap = re.search('(?s)Current Participant List(.*)tbody', allTxt)

#from the table, extract usernames
matchList = re.findall('(users\/\d+">)(.+)(<\/a)', tableCap.group(1))

numUsers = len(matchList)
userList = []

for i in range(numUsers):
    userList.append(matchList[i][1])

print("There are",numUsers,"current active users")
userList = sorted(userList, key=str.casefold)
writeSpace()
print("done!")