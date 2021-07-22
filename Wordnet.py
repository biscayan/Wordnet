from nltk.corpus import wordnet

class Wordnet:

    def dictionary(self):

        syns = wordnet.synsets(input("Input a word : "))

        for i in range(len(syns)):
            print(syns[i].name()," : ",end='')
            print(syns[i].definition())
            print(syns[i].examples())
            print()

    def synonym(self):

        synonyms = set()

        for syns in wordnet.synsets(input("Input a word : ")): 
            for lemma in syns.lemmas():
                synonyms.add(lemma.name()) 

        print("Synonyms : ", synonyms)

    def antonym(self):

        antonyms = set()

        for syns in wordnet.synsets(input("Input a word : ")): 
            for lemma in syns.lemmas():
                if lemma.antonyms():
                    antonyms.add(lemma.antonyms()[0].name())

        print("Antonyms : ", antonyms)

    def hypernym(self):

        hypernyms = set()
        
        for syns in wordnet.synsets(input("Input a word : ")):
            for hyper in syns.hypernyms():
                for lemma in hyper.lemmas():
                    hypernyms.add(lemma.name())

        print("Hypernyms : ", hypernyms)
        
    def hyponym(self):

        hyponyms = set()
        
        for syns in wordnet.synsets(input("Input a word : ")):
            for hypo in syns.hyponyms():
                for lemma in hypo.lemmas():
                    hyponyms.add(lemma.name())

        print("Hyponyms : ", hyponyms)

    def meronym(self):

        meronyms = set()
        
        for syns in wordnet.synsets(input("Input a word : ")):
            for mero in syns.part_meronyms():
                for lemma in mero.lemmas():
                    meronyms.add(lemma.name())

        print("Meronyms : ", meronyms)

    def holonym(self):

        holonyms = set()
        
        for syns in wordnet.synsets(input("Input a word : ")):
            for holo in syns.part_holonyms():
                for lemma in holo.lemmas():
                    holonyms.add(lemma.name())

        print("Holonyms : ", holonyms)

    def entailnemt(self):

        entailments = set()
        
        for syns in wordnet.synsets(input("Input a word : ")):
            for entail in syns.entailments():
                for lemma in entail.lemmas():
                    entailments.add(lemma.name())

        print("Entailnemts : ", entailments)


if __name__ == '__main__':

    word = Wordnet()

    print("1 : Dictionary")
    print("2 : Synonym")
    print("3 : Antonym")
    print("4 : Hypernym")
    print("5 : Hyponym")
    print("6 : Meronym")
    print("7 : Holonym")
    print("8 : Entailnemt")
    print()

    flag = True

    while flag:

        mode = int(input("Choose a relationship(number) that you want to know : "))
        print()
        
        if mode == 1:
            word.dictionary()
        elif mode == 2:
            word.synonym()
        elif mode == 3:
            word.antonym()
        elif mode == 4:
            word.hypernym()
        elif mode == 5:
            word.hyponym()
        elif mode == 6:
            word.meronym()
        elif mode == 7:
            word.holonym()
        elif mode == 8:
            word.entailnemt()
        print()

        another = input("Do you want to know another relationship? (Yes / No) : ")

        if another == "No" or another == "no":
            flag = False