#imports
from os import read


#Dictionary for all words: "Word" = word object

#classes
class Word ():
    def __init__(self, word) -> None:
        self.word = word
        self.fwords = {}
        self.occurs = 1
    

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
    puncList = ["/", "\'", '\"', ")", "("]
    words = {}
    wordGroup = readInLines(txtFile)
    for wordIndex in range(len(wordGroup)):
       
        currentWord = wordGroup[wordIndex]
        #print("Current word is: " + currentWord)
        if wordIndex == len(wordGroup) - 1: #if at end of list
            nextWord = ""
        else:
            nextWord = wordGroup[wordIndex + 1]
            #print(nextWord[0])
            if nextWord in puncList:
                nextWord = nextWord
            elif currentWord in puncList:
                currentWord = currentWord

            else:
                if currentWord[-1:] in puncList: #if last character is punctuation remove punctuation
                    currentWord = currentWord[:-1]
                if nextWord[-1:] in puncList: #if last character is punctuation remove punctuation
                    nextWord = nextWord[:-1]
                if currentWord[0] in puncList: #if first character is punctuation remove punctuation
                    currentWord = currentWord[1:]
                if nextWord[0] in puncList: #if first character is punctuation remove punctuation
                    nextWord = nextWord[1:]
            
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
    
    

    

