from collections import Counter

a = ['base ball', 'base ball', 'base ball', 'base ball', 'base ball', 'base ball', 
'basket ball', 'basket ball', 'basket ball', 'basket ball', 'basket ball', 'basket ball', 'basket ball', 'basket ball', 'basket ball', 
'soccer', 'soccer', 'soccer', 'soccer', 'soccer', 'soccer']

counter = Counter(a)
for key in counter.keys() :
  print(key, counter.get(key))