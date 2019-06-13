from bs4 import BeautifulSoup
import urllib.request as urllib
import requests
import csv

url = "http://sysmonweb/SuperMon/#oncall"
f = open('OnCall.txt', 'w')

re = requests.get(url)
data_list = []

soup = BeautifulSoup(re.text, "lxml")
for item in soup.findAll('table', {'class':'table table-striped table-bordered smart-form dt-custom dataTable'}):
    data_list.append(item.get(re.text))

f.write(str(data_list))
f.close
