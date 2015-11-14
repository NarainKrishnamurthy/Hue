from nltk.corpus import wordnet as wn

def synlist(query):
    list = []
    for synset in wn.synsets(query):
        for lemma in synset.lemmas():
            list.append(lemma.name())
    return list

print "input word: "
print synlist(raw_input())
