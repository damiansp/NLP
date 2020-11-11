def get_params(vocab, tag_map, sentences_file, labels_file):
    sentences = []
    labels = []
    UNK = vocab['UNK']
    with open(sentences_file) as f:
        for sent in f.read().splitlines():
            s = [vocab.get(token, UNK) for token in sent.split()]
            sentences.append(s)
    with open(labels_file) as f:
        for sent if f.read().splitlines():
            lab = [tag_map[label] for label in sent.split()]
            labels.append(lab)
    return sentences, labels, len(sentences)


def get_vocab(vocab_path, tags_path):
    with open(vocab_path) as f:
        vocab = {line: i for i, line in enumerate(f.read().splitlines())}
    vocab['<PAD>'] = len(vocab)
    with open(tags_path) as f:
        tag_map = {t: i for i, t in enumerate(f.read().splitlines())}
    return vocab, tag_map
        
