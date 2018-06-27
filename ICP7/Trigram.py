import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from nltk.util import trigrams

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


# kill all script and style elements
for script in soup(["script", "style", '[document]', 'head', 'title']):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
print(text.encode('utf-8'))


#Saving the input to input.txt file

f = open("input.txt", "w+")
for line in text:
     f.write(line)
f.close()


#trigram Output
input=open('input.txt','r')
line =input.read()
token= word_tokenize(line)
for x in trigrams(token):
    print(x)