# 5. 🧩 The Word Detective
# Ask the user for a sentence.
# Your program should find:

# Number of words
# Longest word
# Shortest word
# Number of unique words
# Most frequently occurring word
# Number of vowels
# Number of consonants
sen= "Python is very beautiful language and Python is very Good"
words = sen.split()
nofwords = len(words)
longword = ""
shortword = ""
sentencewords=[]
shortest_lenght= float("inf")
count = {}
vowel_count = 0
space_count = 0
consonant_count = 0
for eword in words:
    leng = len(eword)
    if len(longword) < leng:
        longword = eword

    if shortest_lenght > leng:
        shortest_lenght = leng
        shortword = eword

    if eword not in sentencewords:
        sentencewords.append(eword)

    if eword in count:
        count[eword] = count[eword] + 1
    else:
        count[eword] = 1

for char in sen:
    if (char == "A" or char == "a" or char == "E" or char =="e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u"):
        vowel_count += 1

    elif(char == " "):
        space_count += 1

    elif char.isalpha(): 
        consonant_count += 1

mostword = ""
mostcount = 0

for word in count:
    if count[word] > mostcount:
        mostcount = count[word]
        mostword = word




print(f"No of Words : {nofwords}")
print(f"Longest Word : {longword}")
print(f"Shortest Word : {shortword}")
print(f"Most Repeated word is {mostword} = {mostcount}")
print("No of Vowels : ",vowel_count)
print("No of Consonants : ",consonant_count)
print("No of Spaces : ",space_count)

