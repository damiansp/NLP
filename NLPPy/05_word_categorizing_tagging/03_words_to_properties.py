import nltk

# Default Dictionaries
frequency = nltk.defaultdict(int)
frequency['colorless'] = 4
frequency['ideas'] # 0 by default

pos = nltk.defaultdict(list)
pos['sleep'] = ['N','V']
pos['ideas'] # [] by default

pos = nltk.defaultdict(lambda: 'N')
pos['colorless'] = 'ADJ'
pos['blog'] #'N' by default
print(pos.items())

alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreDist(alice)
v1000 = list(vocab)[:1000]
mapping = nltk.defaultdict(lambda: 'UNK')

for v in v1000:
    mapping[v] = v

alice2 = [mapping[v] for v in alice]
print(alice2[:100])
