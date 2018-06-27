import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import pos_tag, ne_chunk, wordpunct_tokenize

f = open('input.txt','r')
text = f.readline()
while text!='':
 print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
 text = f.readline()