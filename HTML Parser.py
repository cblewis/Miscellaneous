from bs4 import BeautifulSoup
import urllib.request as urllib
import csv

url = "https://confluence1.daicompanies.com/admin/users/showallusers.action"
f = open('JiraUsers.csv', 'w')

x = 0
while x < 500:
    soup = BeautifulSoup(urllib.urlopen("https://confluence1.daicompanies.com/admin/users/showallusers.action"+str(x)).read(), 'html.parser')
    userlist = soup.find('table', {'class':"aui user-table"})
    for row in userlist.findAll('td')[0:]:
        col = row.findAll('td')
        try:
            name = col[0].a.string.strip()
            f.write(name+'\n')
        except:
            pass
    x+=40
f.close()
