def make_ngrams(text, max_n):
    text = text.split()
    ngrams = {}
    for n in range(1, max_n + 1):
        ngrams[n] = {}
        for i in range(len(text) - n):
            ngram = ' '.join(text[i:i+n])
            if ngram in ngrams[n]:
                ngrams[n][ngram] += 1
            else:
                ngrams[n][ngram] = 1
    return ngrams


text = 'demonstrate that your bigram model does not assign a single ' \
       'probability distribution across all sentence lengths'

print(make_ngrams(text, 3))
