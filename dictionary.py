class Parole:
    def __init__(self,al,it):
        self.alieno=al
        self.parole_alternative=[it]

class Dictionary:
    def __init__(self):
        self.dizionario=[]

    def addWord(self,alieno,ita):
        c=False
        for i in self.dizionario:
            if i.alieno==alieno:
                c=True
                i.parole_alternative.append(ita)
        if c==False:
            self.dizionario.append(Parole(alieno,ita))

    def translate(self,alieno):
        parola=[]
        if len(self.dizionario)>0:
            for i in self.dizionario:
                if i.alieno==alieno:
                    parola = i.parole_alternative
        if len(parola)>0:
            return parola
        else:
            return 'nessuna parola trovata'

    def leggifile(self, file):
        f =open(file,"r")
        for i in f.readlines():
            self.addWord(i.split(" ")[0],i.split(" ")[1].strip("\n"))


    def translateWordWildCard(self):
        pass

    def stampadict(self):
        for i in self.dizionario:
            print(f'alieno: {i.alieno} italiano: {i.parole_alternative}')

    def chiudi_file(self,file):
        f = open(file,'w')
        c =0
        for i in self.dizionario:
            if c==0:
                c+=1
                if len(i.parole_alternative)==1:
                    f.write(f'{i.alieno} {i.parole_alternative[0]}')
                else:
                    for k in i.parole_alternative:
                        f.write(f'{i.alieno} {k}')
            else:
                if len(i.parole_alternative)==1:
                    f.write(f'\n{i.alieno} {i.parole_alternative[0]}')
                else:
                    for k in i.parole_alternative:
                        f.write(f'\n{i.alieno} {k}')

