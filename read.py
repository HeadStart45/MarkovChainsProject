#imports

#classes
class Word ():
    def __init__(self, word) -> None:
        self.word = word
        self.vertexs = {}
        self.occurs = 1
    
    def __str__(self) -> str:
        return self.word
    
    def get_word(self):
        return self.word
    
    def get_vertexs(self):
        return self.vertexs    
    
    def get_occurs(self):
        return self.occurs

    def add_vertex(self, wordObj):
        if wordObj in self.vertexs.keys():
            self.vertexs[wordObj] += 1
        else:
            self.vertexs[wordObj] = 1

def importTxt (txtFile): #returns list of words from .txt file
    puncList = ["(", ")", "\'", "\"", "/"]
    lines = []
    words = []
    with open(txtFile, 'r') as r:
        lines = r.readlines()
    
    for line in lines:
        wordList = line.split()
        for word in wordList:
            if word[-1:] in puncList:
                word = word[:-1]
            if word[0] in puncList: #remove ( ) " ' /
                word = word[1:]
            words.append(word)
    
    return words

def createWordObjList(rawWordList): #returns list of Word objects
    
    wordObjs = []
    for word in rawWordList:
        wordObj = Word(word)
        wordObjs.append(wordObj)

    return wordObjs

def generateVertexs(txtFile): #calculate verticies and add original words to worObjs dictionary
    rawWords = importTxt(txtFile)
    wordObjList = createWordObjList(rawWords)
    wordObjs = {}
    for i in range(len(wordObjList)):
        currentWordObj = wordObjList[i]
        currentWord = currentWordObj.get_word()

        if i < len(wordObjList) - 1:
            nextWordObj = wordObjList[i + 1]
            nextWord = nextWordObj.get_word()
        
            if currentWord not in wordObjs.keys():
                wordObjs[currentWord] = currentWordObj

            if nextWord in wordObjs.keys():
                currentWordObj.add_vertex(wordObjs[nextWord]) #use existing Word Object to add vertex
            else:
                wordObjs[nextWord] = nextWordObj #add original Word Object to list then add vertex
                currentWordObj.add_vertex(wordObjs[nextWord])
       
        else:
            return wordObjs #dictionary
    
        

print(generateVertexs("plan.txt"))
