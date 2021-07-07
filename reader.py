#imports
from os import read


#Dictionary for all words: "Word" = word object

#classes
class Word ():
    def __init__(self, word) -> None:
        self.word = word
        self.fwords = {}
        self.occurs = 1
    def __str__(self) -> str:
        return self.word

    def addVertex(self, word, list):
        if word in list.keys():
            if word in self.fwords.keys():
                self.fwords[list[word]] += 1
            else:
                self.fwords[list[word]] = 1
        else:
            wordObj = Word(word)
            list[word] = wordObj
            self.fwords[list[word]] = 1

    def get_word(self):
        return self.word

#methods

def readInLines(txtFile):
    words = []
    with open(txtFile, 'r') as t:
        lines = t.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        for word in line:
            words.append(word)
    
    return words


def makeChains(txtFile):
    words = {}
    wordGroup = readInLines(txtFile)
    for wordIndex in range(len(wordGroup)):
        puncList = [".", ",", "/", "'", '"', ":", ")"]
        currentWord = wordGroup[wordIndex]
        #print("Current word is: " + currentWord)
        
        if currentWord[-1:] in puncList:
            #if last character is punctuation, add vertex and remove punctuation
            nextWord = currentWord[-1:]
            currentWord = currentWord[:-1]
        elif wordIndex == len(wordGroup) - 1:
            nextWord = "."
        else:
            nextWord = wordGroup[wordIndex + 1]
            if nextWord[-1:] in puncList:
                nextWord = nextWord[:-1]

          
        #print("Next word is: " + nextWord)

        if currentWord in words.keys():
            words[currentWord].addVertex(nextWord, words)
            words[currentWord].occurs += 1
            #print("Adding 1 vertex for " + words[currentWord].word + " to " + nextWord)
        else:
            wordObj = Word(currentWord)
            #print("Creating new word " + wordObj.word)
            words[currentWord] = wordObj
            wordObj.addVertex(nextWord, words)
            
            #print("Adding 1 vertex for " + words[currentWord].word + " to " + nextWord)
    
    
    return words
    
        
        


if __name__ == "__main__":
    worddict = makeChains("tester.txt")
    for word in worddict.keys():
        print(worddict[word].word + ": " + str(worddict[word].occurs))
    
    

    

