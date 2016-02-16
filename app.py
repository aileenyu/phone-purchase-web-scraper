from BeautifulSoup import BeautifulSoup
import requests
import re
import time

regex = {"G4":"400", "G3":"300", "S6":"500", "6P":"650", "5X":"500", "Nexus":"400","Moto":"400"}
BASE_URL = "http://www.kijiji.ca/b-phone-tablet/mississauga-peel-region/c132l1700276"

response = requests.get(BASE_URL)
html =  response.content
soup = BeautifulSoup(html)

#print soup

container = soup.find('div', attrs={"class":"container-results"})

for tableItem in container.findAll('table', attrs={"class": " regular-ad js-hover "}):
    row = tableItem.find('tr')
    #desc = row.find('td', attrs={"class": "description"}).find('a').contents[0].strip()
    link = row.find('td', attrs={"class": "description"}).find('a', href=True)
    href = link['href']
    desc = link.contents[0].strip()
    #print href
    price = row.find('td',attrs={"class":"price"}).contents[0].strip();
    #print desc+" : "+price
    for key,value in regex.iteritems():
        if (re.search(key, desc, re.IGNORECASE)):
            if (value > price):
                print "Found a: "+key+" for: "+price
                print "###   "+href+"   ###"
