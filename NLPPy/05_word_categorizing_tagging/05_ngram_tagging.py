import nltk
from nltk.corpus import brown

# Unigram tagging
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

unigram_tagger.tag(brown_sents[2007])
print(unigram_tagger.evaluate(brown_tagged_sents)) # 93.49 


# Train/Test split
size = int(0.9 * len(brown_tagged_sents)) # 4160
train_sents = brown_tagged_sents[:size]
test_sents  = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents)) # 81.30


# General n-gram tagging
bigram_tagger = nltk.BigramTagger(train_sents)

bigram_tagger.tag(brown_sents[2007])
print(bigram_tagger.evaluate(test_sents)) # 10.21
# lots of combinations don't get included in the model
print(bigram_tagger.tag(brown_sents[4203]))


# Combining taggers
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents,  backoff=t1)
print(t2.evaluate(test_sents)) # 84.60

t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print(t3.evaluate(test_sents)) # 84.50
                  

