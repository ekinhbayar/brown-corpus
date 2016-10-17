# Brown Corpus
This repository holds various exports from Brown Corpus and useful scripts.

Within the /exports directory, you can find raw and deduplicated exports in separate files.
 - Per category exports are located in /exports/categories. Deduplicated exports are sorted alphabetically (case sensitive).
 - The complete (raw) export file is named `raw_lexicon.txt` whereas deduplicated one is named `lexicon.txt` and is also available in JSON format. 
 - All exports are tagged.

You can find the python scripts used to export these within /scripts directory. 
 - Per category export is done with `categories.py`. 
 - The complete export is done with `brown.py`.
 - Part of speech and the respective tag are separated with a single space on each line. Change the line that sets the `text` to modify this as you like.
 
Both scripts generate raw, tagged lexicons and to use them you will need Python versions 2.7 or 3.2+ and `NLTK`.

--

### Resources
[Brown Corpus](https://en.wikipedia.org/wiki/Brown_Corpus) was compiled in the 1960s by Henry Kučera and W. Nelson Francis at Brown University, Providence, Rhode Island as a general corpus (text collection) in the field of corpus linguistics. It contains 500 samples of English-language text, totaling roughly one million words, compiled from works published in the United States in 1961.

 - [Part of Speech Tags](https://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used)
 - [The Brown Corpus Tag Set](http://www.scs.leeds.ac.uk/ccalas/tagsets/brown.html)
 - [Browse Brown Corpus at Open Corpora](https://the.sketchengine.co.uk/open/)
 - [Brown Corpus Manual](http://clu.uni.no/icame/manuals/BROWN/INDEX.HTM)
 - [Python Natural Language Toolkit - NLTK](http://www.nltk.org/)
 - [NLTK Corpora and Models](http://www.nltk.org/nltk_data/)
 - [NLTK repo on GitHub](https://github.com/nltk/nltk)

--

### Installing NLTK

**Mac/Unix**

  -  Install NLTK: `sudo pip install -U nltk`
  -  Install Numpy (optional): `sudo pip install -U numpy`
  -  Test installation: run `python` then type `import nltk`

For older versions of Python it might be necessary to install [setuptools](http://pypi.python.org/pypi/setuptools) and to install pip run `sudo easy_install pip`.

--

**Windows**
32-bit binary installation

  -  Install [Python 3.4](http://www.python.org/downloads/) (avoid the 64-bit versions)
  -  Install [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/) (optional) (the version that specifies python3.4)
  -  Install [NLTK](http://pypi.python.org/pypi/nltk)
  -  Test installation: `Start>Python34`, then type `import nltk`

--

Thanks to [ulgens](https://github.com/ulgens) and [JonathanReeve](https://github.com/JonathanReeve) for their examples.
