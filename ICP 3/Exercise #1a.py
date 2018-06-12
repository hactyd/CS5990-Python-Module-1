sentence = input("What is your sentence?")



def w_count(str):
    number = dict()
    wordz = str.split()
    for word in wordz:
        if word in number:
            number[word] += 1
        else:
            number[word] = 1


    return number


print(w_count(sentence))



