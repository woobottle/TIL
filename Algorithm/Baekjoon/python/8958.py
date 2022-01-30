import sys
input = sys.stdin.readline

def BOJ8958() :
  T = int(input())
  for _ in range(T) :
    l = list(input())
    score = 0
    if l[0] == 'O' :
      score = 1
    temp = 1
    
    for i in range(1, len(l)) :
      if l[i] == 'O' :
        if l[i-1] == 'O' :
          temp += 1
          score += temp
        else :
          temp = 1
          score += temp
      else :
        continue
    print(score)

BOJ8958()
