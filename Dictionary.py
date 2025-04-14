class Dictionary:
    
    def __init__(self):
        self.dict={}

    def newentry(self, word, entry):
        self.dict[word]=entry
                
    def look(self,word):
        if word in self.dict:
            return self.dict[word]
        else:
            return "Can't find entry for " + word                    


if __name__ == "__main__":
    obj = Dictionary()
    obj.newentry('Apple','A fruit that grows on trees')
    print(obj.look('Apple'))
    print(obj.look('Banana'))
