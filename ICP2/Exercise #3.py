
wordCount = 0
file = open("inputFile2", 'r')
for line in file:
    words = line.split()
    wordCount += len(words)
    print(line, wordCount)
    wordCount = 0
