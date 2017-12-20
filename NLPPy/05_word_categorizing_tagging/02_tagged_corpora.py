import nltk

# Representing tagged tokens
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token) # ('fly', 'NN')

# Reading tagged corpora
print(nltk.corpus.brown.tagged_words()[:10])
print(nltk.corpus.nps_chat.tagged_words()[:10])

