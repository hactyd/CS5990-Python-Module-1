input = input("Please enter a sentence: ")
vowel = 0

for i in input:
    if (i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'O' or i == 'U'):
        vowel += 1
print("The number of vowels is: ")
print(vowel)
