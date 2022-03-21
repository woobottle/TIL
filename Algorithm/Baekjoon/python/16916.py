import sys
input = sys.stdin.readline

def BOJ16916() :
  # 접두사와 접미사 개념
  def make_table(pattern) :
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)) :
      while j > 0 and pattern[i] != pattern[j] :
        j = table[j-1]
      if pattern[i] == pattern[j] :
        j += 1
        table[i] = j

    return table

  def KMP(parent, pattern, table) :
    j = 0

    for i in range(len(parent)) :
      while j > 0 and parent[i] != pattern[j] :
        j = table[j-1]
      
      if parent[i] == pattern[j] :
        if j == len(pattern) - 1 :
          return True
        
        j += 1

    return False

  S = input().strip()
  P = input().strip()
  table = make_table(P)
  
  if (KMP(S, P, table)) :
    print(1)
  else :
    print(0)

BOJ16916()
