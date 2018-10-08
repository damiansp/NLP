#import spacy
from nltk.tokenize import TweetTokenizer

#nlp = spacy.load('en')
#text = "Mary, don't slap the green witch."
#print([str(token) for token in nlp(text.lower())])

tweet = u'Snow White and the Seven Degrees #MakeAMovieCold @midnight :-)'
tokenizer = TweetTokenizer()
print(tokenizer.tokenize(tweet.lower()))
