import argparse
import collections
import string
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default=None, help='The file to be n-grammed')
parser.add_argument('-mi', '--minimum', type=int, default=1, help='The minimum ngram length to parse.')
parser.add_argument('-ma', '--maximum', type=int, default=1, help='The maximum ngram length to parse.')
args = parser.parse_args()        

def ngram(string,nmin,nmax):
  ngrams = []
  words = string.split()

  for n in range(nmin,nmax+1):
   grams = [words[i:i+n] for i in range(len(words)-n+1)]
   
   for gram in grams:
      gram = ' '.join(str(w) for w in gram)
      ngrams.append(gram)
  return ngrams
  
with open(args.file, 'r') as myfile:
    data = myfile.read().replace('\n', ' ')
    
translator = str.maketrans('', '', string.punctuation)
data = data.translate(translator)
    
try:
	for k, v in sorted(((value, key) for (key,value) in collections.Counter(ngram(data,args.minimum,args.maximum)).items()), reverse=True):
		print('{0} \t {1}'.format(k,v))
except (BrokenPipeError, IOError):
    pass

sys.stderr.close()