class ArrayOfWords:
    
    def __init__(self):
        pass

    def concatenate_words(self, wordsArray):
        finalWord=''
        n=0
        try:
            for word in wordsArray:
                finalWord+= word[n]
                n+=1
            return finalWord
        except IndexError:
            return "Error, out of bounds (not enough letters)"
            
if __name__ == "__main__":
    AOW = ArrayOfWords()
    print(AOW.concatenate_words(['yoda', 'best', 'has']))