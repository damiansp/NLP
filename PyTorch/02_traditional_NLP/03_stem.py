import spacy

nlp = spacy.load('en')
doc = nlp(u'he went running later')

for token in doc:
    print('{} -> {}'.format(token, token.pos_, token.lemma_))
