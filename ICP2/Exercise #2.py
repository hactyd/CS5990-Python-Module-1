
"""samplefile = open("inputFile").read()

for word in samplefile.split():

   wordlen = str(len(word))

   print(word + " " + wordlen)"""


lenChar = 0
file2 = open("writefile", "w+")
with open("inputFile", 'r') as file:
    for line in file:
        for char in line:
            lenChar = lenChar + 1
            strLenChar = str(lenChar - 1)
        file2.write(line)
        file2.write(strLenChar)
        file2.write((" \n"))
        print(line, lenChar-1)
        lenChar = 0
        i = 0






