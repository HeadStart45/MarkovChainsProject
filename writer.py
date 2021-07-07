#imports
from os import write
from PySimpleGUI.PySimpleGUI import Button, WINDOW_CLOSED
import reader
import PySimpleGUI as sg
from random import choices
from random import randint
from os import path

#global containers
WORDS = [] #passed into random.choices with wordchances as weights
WORDCHANCES = []

puncList = [".",",", "/", "\'", '\"', ":", ")", "("]

#methods
def startingWords(chainList):
    WORDS.clear()
    WORDCHANCES.clear()
    for key in chainList.keys():
        WORDS.append(key)
        WORDCHANCES.append(chainList[key].occurs)

def importChain(textFile):
    chains = reader.makeChains(textFile)
    startingWords(chains)
    return chains

def chooseNextWord(word, chains):
    wordObj = chains[str(word)]
    words = []
    chances = []
    #key is words, value is chances
    if len(wordObj.fwords.keys()) != 0:
        #print("Ping")
        for key in wordObj.fwords.keys():
            words.append(key)
            chances.append(wordObj.fwords[key])
    else:
        words = WORDS
        chances = WORDCHANCES

    nextWord = choices(words, chances, k=1)
    return nextWord[0]


def writePoem(textFile):
    chains = importChain(textFile)
    poem = ""
    for i in range(randint(2, 4)):
        starter = choices(WORDS, WORDCHANCES, k=1)
        currWord = starter[0]
        line = ""
        for i in range(randint(5, 8)):
            if i == 0:
                line += str(str(currWord).capitalize())
            elif str(currWord) in puncList:
                line += ".\n"
                break
            else:
                line += str(" " + str(currWord))
            testWord = str(currWord)
            if str(testWord[-1:]) in puncList:
                currWord = testWord[:-1]
            try:
                currWord = chooseNextWord(currWord, chains)
            except:
                currWord = choices(WORDS, WORDCHANCES, k=1)[0]
        if line[-1:] != "\n":
            line += '\n'
        poem += line
    return poem

class Seed():
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
    def __str__(self) -> str:
        return self.name
    
    def get_path(self):
        return self.address

seeds = []

path_to_lotr = path.abspath(path.join(path.dirname(__file__), 'lotr.txt'))
path_to_hp1 = path.abspath(path.join(path.dirname(__file__), 'hp1.txt'))

lotr = Seed("Lord of the Rings", path_to_lotr)
seeds.append(lotr)
hp1 = Seed("Harry Potter and the Philosphers Stone", path_to_hp1)
seeds.append(hp1)

def seedPicker ():
    
    layout = [[sg.Text("Pick from included seeds: ")],
            [sg.Listbox(values=seeds, key="-Seed-", enable_events=True, size=(50,10)), sg.Button("Go!")],
            [sg.Text("Or")],
            [sg.Text("Choose your own .txt file: "), sg.Button("Browse")]]

    window = sg.Window("Seed Picker", layout)

    while True:
        event, values = window.read()

        if event in ("Exit", WINDOW_CLOSED):
            break
        elif event in ("-Seed-", "Go!"):
            window.close()
            return values["-Seed-"][0]
        elif event == "Browse":
            sname = sg.popup_get_file("Select .txt File")
            seed = Seed(sname, sname)
            window.close()
            return seed
            

    window.close()

def main():
    fnameObj = seeds[1]
    layout =[[sg.Text("Poem Generator"), sg.Text("Current Seed: "), sg.Text(size=(30,1),key="-seedname-", text="Harry Potter and the Philosphers Stone")],
            [sg.Multiline(size=(60, 40), background_color="black", text_color="white", key="-Out-") ],
            [sg.Button("New Seed")],
            [sg.Button("Generate"), sg.Button("Exit")]]
    window = sg.Window("Generator", layout)

    while True:
        event, values = window.read()
        window["-seedname-"].update(fnameObj)

        if event in ("Exit", WINDOW_CLOSED):
            break
        elif event == "Generate":
            print(fnameObj.get_path())
            window["-Out-"].update(writePoem(fnameObj.get_path()))
        elif event == "New Seed":
            fnameObj = seedPicker()
            
            
            

            
    window.close()


if __name__ == "__main__":
    main()
