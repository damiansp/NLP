import nltk

text = nltk.word_tokenize('And now for something completely different')
print(nltk.pos_tag(text))

text = nltk.word_tokenize('they refuse to permit us to obtain a refuse permit')
print(nltk.pos_tag(text))

# Key:
# CC: coordinate conjuntion RB:  adverb           IN: preposition   NN: Noun
# JJ: Adjective             PRP: personal pronoun VBP: verb-present TO: 'to'
# VB: verb                  DT:  determiner


