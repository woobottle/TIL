def solution(beginWord, endWord, wordList) :
  if (endWord not in wordList) :
    return 0
  
  answer = []
  def count_distance(firstWord, secondWord):
    return len(set(list(firstWord)) - set(list(secondWord)))

  def check(beginWord, endWord, wordList, count) :
    if(beginWord == endWord) :
      answer.append(count)
      return 
    else :
      for word in wordList :
        if(count_distance(beginWord, word) == 1) :
          wordList.remove(word)
          check(word, endWord, wordList, count + 1)
          wordList.append(word)
  
  check(beginWord, endWord, wordList, 1)
  return min(answer)

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
