import dictionary as dx

class Translator:

    def __init__(self):
        self.d = dx.Dictionary()

    def printMenu(self):
        print("-----------------------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-----------------------------------------------")
        print()


    def loadDictionary(self, dict):
        self.d.leggifile(dict)

    def handleAdd(self, entry):
        self.d.addWord(entry[0], entry[1])

    def handleTranslate(self, query):
        i= self.d.translate(query)
        return i

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def stampa(self):
        self.d.stampadict()

    def aggiuntamultipla(self,listina):
        for i in listina:
            if i!=listina[0]:
                self.d.addWord(listina[0],i)
    def exits(self,file):
        self.d.chiudi_file(file)