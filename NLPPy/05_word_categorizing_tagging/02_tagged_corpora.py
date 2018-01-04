import nltk
from nltk.corpus import brown

# Representing tagged tokens
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token) # ('fly', 'NN')

# Reading tagged corpora
print(brown.tagged_words()[:10])
print(nltk.corpus.nps_chat.tagged_words()[:10])

brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.keys())

word_tag_pairs = nltk.bigrams(brown_news_tagged)
print(list(nltk.FreqDist(a[1] for a, b in word_tag_pairs if b[1] == 'N')))

wsj = nlt.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
print([word + '/' + tag for word, tag in word_tag_fd if tag.startswith('V')])



      


