import nltk
from nltk.corpus import brown

words = brown.tagged_words()
text = '\n'.join('%s %s' % word for word in words)
filename = 'brown.txt'
with open(filename, 'w') as outfile:
    outfile.write(text)
