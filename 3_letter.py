wordList = []

with open("words.txt", "r") as words:
    
    word = words.readlines()
    wordList.append(word)

print(wordList)
#def separate_word(wordList, word):
    #for i in range(4):
        #wordList.append(word[i])

    #print(wordList)

#separate_word(wordList, word)    

