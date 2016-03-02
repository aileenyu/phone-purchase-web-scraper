from BeautifulSoup import BeautifulSoup
import requests
import re
import time
from datetime import datetime

def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

regex = {"G4":400, "G3":225, "S6":500, "6P":650, "5X":500, "Nexus":400,"Moto":400, "OnePlus":500,"One Plus":500}
BASE_URL = "http://www.kijiji.ca/b-phone-tablet/kitchener-waterloo/"
ENDING = "/c132l1700212"
GREEN = '\033[92m'
RED = "'\033[91m'"
BLUE = '\033[94m'
ENDC = '\033[0m'

print "How many pages: ",
times = input()
while True:
    print "Results for " + BLUE + datetime.strftime(datetime.now(), '%H:%M:%S')+ENDC
    for i in xrange(1,times+1):
        print BASE_URL+"page-"+str(i)+ENDING
        response = requests.get(BASE_URL+"page-"+str(i)+ENDING)
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
            price = row.find('td',attrs={"class":"price"}).contents[0].strip()[1:]
            if(isFloat(price)):
                for key,value in regex.iteritems():
                    if (re.search(key, desc, re.IGNORECASE)):
                        if (value > float(price)):
                            print "Found a: "+BLUE+key+ENDC+" for: "+GREEN+price+ENDC
                            print "###   "+href+"   ###"
                            if (value-float(price)>=100):
                                print RED+"###GOOD DEAL###"+ENDC
    time.sleep(900)
