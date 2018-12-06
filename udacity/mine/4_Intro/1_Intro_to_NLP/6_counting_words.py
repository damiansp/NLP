'''Count words.'''
import re


def count_words(text):
    '''Count how many times each unique word occurs in text.'''
    counts = {}  # dictionary of { <word>: <count> } pairs to return
    text = text.lower()
    text = re.compile('\W+').split(text)
    for word in text:
        if word in counts:
            counts[word] += 1
        elif word != '':
            counts[word] = 1
    return counts


def test_run():
    with open("../../data/input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(
            counts.items(), key=lambda pair: pair[1], reverse=True)
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
