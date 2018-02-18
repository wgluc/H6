# 507/206 Homework 6 Part 1

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here
import requests
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

imgs = soup.find_all("img")

for i in imgs:
    if "alt" in i.attrs:
        print(i['alt'])
    else:
        print("No tag")
