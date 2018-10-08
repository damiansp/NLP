import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')


# Default tagger
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags).max())

raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN') # Tags everything as 'NN'
print(default_tagger.tag(tokens))
print(default_tagger.evaluate(brown_tagged_sents)) # 13.1%


# Regex tagger
patterns = [(r'.*ing$', 'VBG'),              # gerunds
            (r'.*ed$', 'VBD'),               # simple past
            (r'.*es$', 'VBZ'),               # 3rd person sg present
            (r'.ould$', 'MD'),               # modals
            (r'.*\'s$', 'NN$'),              # possesive nouns
            (r'.*s$', 'NNS'),                # plural nouns
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
            (r'.*', 'NN')]                   # nouns (default)
regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print(regexp_tagger.evaluate(brown_tagged_sents)) # 20.3%


# Lookup tagger
#fd = nltk.FreqDist(brown.words(categories='news'))
#cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#most_freq_words = fd.keys()[:100] # synax error
#likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
#baseline_tagger = nltk.UnigramTagger(model=likely_tags)
#print(baseline_tagger.evaluate(brown_tagged_sents))

