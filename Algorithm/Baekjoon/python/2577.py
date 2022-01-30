import sys
input = sys.stdin.readline

def BOJ2577() :
  A = int(input())
  B = int(input())
  C = int(input())

  l = {}
  for i in range(10) :
    l[f'{i}'] = 0
  
  for i in list(str(A * B * C)) :
    l[i] += 1
  
  for i in l.values() :
    print(i)

BOJ2577()
