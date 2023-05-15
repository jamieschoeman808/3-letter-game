#This currently accesses a file containing all 3 letter words according to the collins dictionary. 
wordList=[] #This list will store all the words
threeLetterWordList = []
pointList = [] #This list will store all the point values. Although we won't be using it now, we will keep it in case we require it in the future
with open("words.txt", "r") as wordsRaw: #open the file and save it to the file object wordsRaw
    words = wordsRaw.readline() #The readline method returns a list
    words = words.strip() #We use strip to remove any potential whitepace at the front or end of the string

    for i in words:
        try:
           pointList.append(int(i)) #We add all number values to the pointList
        except ValueError: #if the int function is called on a string and an int is not returned, we receive a ValueError
            wordList.append(i)#we know its a letter and add it to wordList


for i in range(1007):
    word = wordList[0]+wordList[1]+wordList[2]
    threeLetterWordList.append(word)
    wordList.remove(wordList[0])
    wordList.remove(wordList[0])
    wordList.remove(wordList[0])


print(threeLetterWordList)


