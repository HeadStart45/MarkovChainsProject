from random import choices
from random import randint
import reader

path = "tester.txt"

def chooseAnyWord(wordDict):
    words = []
    wordChances = []
    for key in wordDict:
        words.append(key)
        wordChances.append(wordDict[key].occurs)
    
    word = choices(words, wordChances)
    word = word[0]
    return word

def chooseNextWord(word, wordDict):
    if len(wordDict.keys()) == 0:
        wordObj = wordDict[word]

        words = []
        wordChances = []

        for key in wordObj.fwords.keys():
            words.append(key)
            wordChances.append(wordObj.fwords[key])
        
        word = choices(words, wordChances)
        
        return word[0].word
    else:
        return chooseAnyWord(wordDict)

def writePoem(txtFile):
    wordDict = reader.makeChains(txtFile) #import dictionary
    lines = ""
    for i in range(2, 5): #lines
        word = chooseAnyWord(wordDict)
        line = word.capitalize() + " "
        for x in range(5, 11):
            word = chooseNextWord(word, wordDict)
            line += word + " "
            if word[-1:] == ".":
                break
        if line[-2:][0] != ".":
            line = line[:-1]
            line + "."
        line += "\n"
        lines += line
    return lines

print(writePoem("tester.txt"))
    




