import urllib.request
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

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


#tokenization steps on the input.txt file

file = open('input.txt', 'rt')
myTokenInput = file.read()
tokenOutput = myTokenInput.split()
print("\n\n","tokenized output is: ", "\n", tokenOutput)
file.close()

#Lemmatising on the input.txt file
lemmatiser = WordNetLemmatizer()
print("\n\n","Lemmatised Output is:")
for w in tokenOutput:
    print(lemmatiser.lemmatize(w))
