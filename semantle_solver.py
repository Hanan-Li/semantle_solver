import nltk
import string
import gensim

from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim.models import Word2Vec as w2v

# constants
PATH = '/path/to/GoogleNews-vectors-negative300.bin'
print("Loading Model")
model = gensim.models.KeyedVectors.load_word2vec_format(PATH, binary=True)
print("Finished Loading Model")

words = []
keys = []
for idx in range(3000000):
    keys.append(model.index_to_key[idx])
while True:
    print("Please Enter Word and Similarity(Format: word similarity):")
    word_similarity = input()
    word = word_similarity.split()[0]
    similarity = float(word_similarity.split()[1]) / 100
    words.append((word, similarity))
    potential_words = []
    for key in keys:
        if abs(similarity - model.similarity(key, word)) <= 0.01:
            potential_words.append(key)
    keys = []
    for pot_word in potential_words:
        if pot_word.isalnum():
            keys.append(pot_word)
    print(keys)
