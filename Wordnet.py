from nltk.corpus import wordnet

class Wordnet:

    #Dictionary
    def dict(self):
        syns=wordnet.synsets(input("Input a word : "))
        for i in range(len(syns)):
            print(syns[i].name()," : ",end='')
            print(syns[i].definition())
            print(syns[i].examples())
            print()

    #Synonym and antonym
    def syn_ant(self):
        synonyms =[]
        antonyms =[]

        for syn in wordnet.synsets(input("Input a word : ")): 
            for lemma in syn.lemmas():
                synonyms.append(lemma.name()) 
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

        print("Synonyms : ",set(synonyms))
        print("Antonyms : ",set(antonyms))

    #Hypernym
    def hyper(self):
        syns_target=wordnet.synset(input("Input a synset : "))
        syns_hyper=syns_target.hypernyms()
        for hyper in syns_hyper:
            for lemma in hyper.lemmas():
                print("Hypernym : ",lemma.name())

    #Hyponym
    def hypo(self):
        syns_target=wordnet.synset(input("Input a synset : "))
        syns_hypo=syns_target.hyponyms()
        for hypo in syns_hypo:
            for lemma in hypo.lemmas():
                print("Hyponym : ",lemma.name())

    #Meronym
    def mero(self):
        syns_target=wordnet.synset(input("Input a synset : "))
        syns_mero=syns_target.part_meronyms()
        for mero in syns_mero:
            for lemma in mero.lemmas():
                print("Meronym : ",lemma.name())

    #Holonym
    def holo(self):
        syns_target=wordnet.synset(input("Input a synset : "))
        syns_holo=syns_target.part_holonyms()
        for holo in syns_holo:
            for lemma in holo.lemmas():
                print("Holonym : ",lemma.name())

    #Entailment
    def entail(self):
        syns_target=wordnet.synset(input("Input a synset : "))
        syns_entail=syns_target.entailments()
        for entail in syns_entail:
            for lemma in entail.lemmas():
                print("Entailment : ",lemma.name())

if __name__ == '__main__':

    word=Wordnet()