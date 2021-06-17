# In the Name of God!

# Get a text from input
text = input()
# print ("Your Input text is : " + text)

# Remove commas
text = text.split(',')
# print ("Splited text by ',' is : ") 
# print (text)

# Join list in to a string 
text = ' '.join(text)
# print ("joied list in to a string :" + text)


# split text in to sentenses 
text = text.split('.')
# print ("Splited text by '.' is : ") 
# print (text)

# split each sentnce into words
words_of_text = []
for word in text:
    word = word.strip()
    words_of_text.append(word.split(" "))
# print ("words : ")
# print(words_of_text)

# First words of each sentence are not a special words , so let remove them
for sentence in words_of_text:
    sentence.pop(0)
# print(words_of_text)

# Difine a dictionanrty for save specila words with numbers of them
special_words = {}

# check for titled words
def check_word (word):
    if word.istitle():
        if word in special_words:
            special_words[word][1] += 1
        else:
            special_words[word] = [word,1]

# Sendeing words
for sentence in words_of_text:
    for word in sentence:
        check_word(word)
# print(special_words)

# printing results 
special_words_list = list(special_words.values()) # Copy special words dictionary in to a list

print("\n-------------------------\nNumber of special words: \n")

# Checking if list is empty
if len(special_words_list) == 0:
    print ("None")
else:
    # Sorting the list 
    special_words_list = sorted(special_words_list, key = lambda x: (-x[1], x[0]))

    #Finally :)
    for word in special_words_list:
        print(str(word[1]) + ":" + word[0])


# split each sentnce into words
words_of_text = []
for word in text:
    word = word.strip()
    words_of_text.append(word.split(" "))
words_of_text.pop(len(words_of_text) - 1)
# print ("words : ")
# print(words_of_text)

# Check for special words
special_words=[]
counter_words=0
for sentence in words_of_text:
    for word in sentence:
        counter_words += 1
        if word.istitle() and sentence.index(word) != 0:
            special_words.append([counter_words,word])
# print ("special words : ")
# print(special_words)

print("\n-------------------------\nThe Place of special words :\n")
# printing results 
# Checking if list is empty
if len(special_words) == 0:
    print ("None")
else:
    # Sorting the list 
    special_words_list = sorted(special_words, key = lambda x: (x[0], x[1]))

    #Finally :)
    for word in special_words_list:
        print(str(word[0]) + ":" + word[1])



# by @JopperKing