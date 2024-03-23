import math


def calculate_tf(word, document):
    words_in_document = document.split()
    word_count = words_in_document.count(word)
    total_words = len(words_in_document)
    return word_count / total_words


def calculate_idf(word, documents):
    word_count = sum(1 for doc in documents if word in doc.split())
    return math.log(len(documents) / (word_count + 1))


def clean_word(word: str):
    while True:
        if ',' in str(word):
            word = word.replace(',', '')
        elif '(' in str(word):
            word = word.replace('(', '')
        elif ')' in str(word):
            word = word.replace(')', '')
        elif ';' in str(word):
            word = word.replace(';', '')
        elif '?' in str(word):
            word = word.replace('?', '')
        elif ':' in str(word):
            word = word.replace(':', '')
        elif '.' in str(word):
            word = word.replace('.', '')
        elif '"' in str(word):
            word = word.replace('"', '')
        elif '!' in str(word):
            word = word.replace('!', '')
        else:
            break

    return word
