import urllib.request
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk import pos_tag

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

#Stemming on the input.txt file
ps = PorterStemmer()
print("\n\n","Stemming Output is:")
#f = open("stemOutput.txt", "w+")
for w in tokenOutput:
    k = ps.stem(w)
    #f.write(k)
    print(k)
#f.close()


#PARTS OF SPEECH tagger
tokens_pos = pos_tag(tokenOutput)
print(tokens_pos)