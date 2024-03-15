import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")
while(True):

    alfa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z',' ']
    t.printMenu()

    txtIn = input("inserire comando da 1 a 5:")

    # Add input control here!

    if int(txtIn) == 1:
        i = input("inserire parola aliena e traduzione:")
        for j in i:
            if j.lower() not in alfa:
                raise ValueError("caratteri/e inesistente")

        if len(i.split(' '))>2:
            l=[]
            for j in i.split(' '):
                l.append(j.strip("\n"))
            t.aggiuntamultipla(l)
        else:
            t.handleAdd((i.split(" ")[0].lower(),i.split(" ")[1].lower()))
        print('Aggiunta')

    if int(txtIn) == 2:
        i2 = input('Parola aliena da cercare:')
        for j in i2:
            if j.lower() not in alfa:
                raise ValueError("caratteri/e inesistente")

        tradotta=t.handleTranslate(i2.lower())
        print(f'Traduzione: {tradotta}')
    if int(txtIn) == 3:
        parola = input("inserire parola con un ? :")
        t.handleWildCard(parola)

    if int(txtIn) == 4:
        t.stampa()
    if int(txtIn) == 5:
        t.exits('dictionary.txt')
        print('arrivederci')
        break
