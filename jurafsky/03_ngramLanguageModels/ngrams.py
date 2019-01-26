import re


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


def cap_sentences(text):
    text = re.split('[\.\?!;]', text)
    if text[-1] == '':
        text = text[:-1]
    text = [f'<s> {s} </s>' for s in text]
    return re.sub('\s+', ' ', ' '.join(text)).strip().lower()


text = 'Demonstrate that your bigram model does not assign a single ' \
       'probability distribution across all sentence lengths.  Why would you ' \
       'do such a thing?  The reasons are twofold.  Because it\'s fun; ' \
       'because you\'ll love it. Now get to work!'

capped = (cap_sentences(text))
print(capped)
print(make_ngrams(capped, 3))
