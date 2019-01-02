# An n-gram parser, which takes a text file and produces a frequency 
# histogram of n-grams with a given minimum and maximum length.

import argparse
import collections
import string
import sys

# Store arguments in parser for input into ngram function.
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default=None, help='The file to be n-grammed')
parser.add_argument('-mi', '--minimum', type=int, default=1, help='The minimum ngram length to parse.')
parser.add_argument('-ma', '--maximum', type=int, default=1, help='The maximum ngram length to parse.')
args = parser.parse_args()        

# Parse string for all phrases containing between nmin and nmax words.
def ngram(string,nmin,nmax):
  ngrams = []
  words = string.split()

  for n in range(nmin,nmax+1):
   grams = [words[i:i+n] for i in range(len(words)-n+1)]
   
   for gram in grams:
      gram = ' '.join(str(w) for w in gram)
      ngrams.append(gram)
  return ngrams

# Open and store text data as a single string, replacing newlines for spaces.
with open(args.file, 'r') as myfile:
    data = myfile.read().replace('\n', ' ')
  
# Remove all punctuation from data to be parsed.  
translator = str.maketrans('', '', string.punctuation)
data = data.translate(translator)

# Run ngram on data, using minimum and maximum arguments, then input 
# into collections.Counter to produce a dictionary with frequency as 
# values. Lastly, sort the dictionary by value and print as formatted.
try:
	for k, v in sorted(((value, key) for (key,value) in collections.Counter(ngram(data,args.minimum,args.maximum)).items()), reverse=True):
		print('{0} \t {1}'.format(k,v))
except (BrokenPipeError, IOError): # Suppress a BrokenPipeError caused if piped with a command like 'head'.
    pass

sys.stderr.close()