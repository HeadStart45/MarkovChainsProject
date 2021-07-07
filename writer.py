from random import choices
import reader

def chooseAnyWord(wordDict):
    words = []
    wordChances = []
    for key in wordDict:
        words.append(key)
        wordChances.append(wordDict[key].occurs)
    
    word = choices(words, wordChances)
    return word[0]

def chooseNextWord(word, wordDict):
    wordObj = wordDict[word]

    words = []
    wordChances = []

    for key in wordObj.fwords.keys():
        words.append(key)
        wordChances.append(wordObj.fwords[key])
    
    word = choices(words, wordChances)
    return word[0]

def writePoem():
    pass

print(chooseNextWord("Liam", reader.makeChains("tester.txt")))