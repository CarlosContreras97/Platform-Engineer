class ArrayOfWords:
    
    def __init__(self):
        pass

    def concatenate_words(self, wordsArray):
        finalWord=''
        n=0
        for word in wordsArray:
            finalWord+= word[n]
            n+=1
        return finalWord
            
            

AOW = ArrayOfWords()
print(AOW.concatenate_words(['yoda', 'best', 'has']))