def n_grams(text, n):
    return [text[i:i + n] for i in range(len(text) - n + 1)]

cleaned = ['mary', ',', "n't", 'slap', 'green', 'witch', '.', '<EOS>']
print(n_grams(cleaned, 3))

            
