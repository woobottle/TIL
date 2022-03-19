from itertools import combinations
import sys
input = sys.stdin.readline

def BOJ1062() :
  def replace_antatica(words) :
    words = words.replace('a', '')
    words = words.replace('n', '')
    words = words.replace('t', '')
    words = words.replace('i', '')
    words = words.replace('c', '')

    return words

  N, K = map(int, input().split())
  words = []
  for _ in range(N) :
    words.append(input().strip())
  
  if K < 5 :
    print(0)
    return

  alphabet = set();
  
  for word in words :
    for i in word :
      alphabet.add(i)
  
  replaced_words = []
  for word in words :
    replaced_words.append(replace_antatica(word))

  words_without_prefix = list(filter(lambda x : x not in list('antatica'), alphabet))

  if len(words_without_prefix) == 0 :
    print(N)
    return 

  word_combinations = combinations(words_without_prefix, min(K - 5, len(words_without_prefix)))

  max_words = 0
  for combination in list(word_combinations) :
    count = 0
    for word in replaced_words :
      for i in combination : 
        word = word.replace(i, '')
      if not word :
        count += 1
    max_words = max(max_words, count)

  print(max_words)

BOJ1062()
