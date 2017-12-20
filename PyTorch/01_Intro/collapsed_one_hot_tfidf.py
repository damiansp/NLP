import matplotlib
matplotlib.use('TkAgg') # seaborn not compatible with default backend

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


corpus = ['Time flies like an arrow', 'Fruit flies like a banana']
one_hot_vectorizer = CountVectorizer(binary=True)
one_hot = one_hot_vectorizer.fit_transform(corpus).toarray()

sns.heatmap(one_hot,
            annot=True,
            cbar=False,
            xticklabels=sorted(one_hot_vectorizer.vocabulary_),
            yticklabels=['S1', 'S2'])
plt.show()


# TF-IDF heatmap
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus).toarray()

sns.heatmap(tfidf,
            annot=True,
            cbar=True,
            xticklabels=sorted(one_hot_vectorizer.vocabulary_),
            yticklabels=['S1', 'S2'])
plt.show()
