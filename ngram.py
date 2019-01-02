import argparse
import collections

text = "This is a great \n set of texts for me great \n set is a great \n this is a great set of texts fun times great \n set going on what silly."

def ngram(string,nmin,nmax):
  ngrams = []
  words = string.replace('\n','').split()

  for n in range(nmin,nmax+1):
   grams = [words[i:i+n] for i in range(len(words)-n+1)]
   
   for gram in grams:
      gram = ' '.join(str(w) for w in gram)
      ngrams.append(gram)
  return ngrams

for k, v in sorted(((value, key) for (key,value) in collections.Counter(ngram(text,1,2)).items()), reverse=True):
  print('{0} \t {1}'.format(k,v))