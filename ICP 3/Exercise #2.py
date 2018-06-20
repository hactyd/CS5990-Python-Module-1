from bs4 import BeautifulSoup
import urllib
from urllib import urlopen
import os
# define the variable and put the link
url="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = urllib.urlopen(url).read()
plain_text = source
#Parse the source code using the Beautiful Soup library and save the parsed code in a variable
soupv = BeautifulSoup(plain_text, "html.parser")
# print the title and the tags
print(soupv.title.string)
for link in soupv.find_all('a'):
    print(link.get('href'))
#detected the table and extracted the td and th elements by iterarting over tr attribute
table1 = soupv.find('table', {'class': "wikitable sortable plainrowheaders"})
for row in table1.find_all('tr')[1:]:
    columns = row.find_all('td')
    header = row.find('th')
    for column in columns:
        print("<td's>: %s"%(column.text))
    print("<th's>: %s"%(header.text))