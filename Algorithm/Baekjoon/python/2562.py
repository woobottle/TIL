import sys
input = sys.stdin.readline

def BOJ2562() :
  l = []
  for _ in range(9) :
    l.append(int(input()))
  print(max(l))
  print(l.index(max(l)) + 1)

BOJ2562()
