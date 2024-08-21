import nltk
from nltk import word_tokenize
from nltk import FreqDist

data = "My name is Arihant. I am a "
wt = word_tokenize(data)

freq = FreqDist(wt)
print(freq.most_common(7))

