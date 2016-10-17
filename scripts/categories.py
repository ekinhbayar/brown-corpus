import nltk
from nltk.corpus import brown

for category in brown.categories():
    words = brown.tagged_words(categories=category)
    text = '\n'.join('%s %s' % word for word in words)
    filename = category + '.txt'
    with open(filename, 'w') as outfile:
        outfile.write(text)
