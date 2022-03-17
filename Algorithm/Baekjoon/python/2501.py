import sys
input = sys.stdin.readline

def BOJ2501() :
  N, K = map(int, input().split())
  l = []
  for i in range(1, N+1) :
    if N % i == 0 :
      l.append(i)
  
  if len(l) < K :
    print(0)
  else :
    print(l[K-1])

BOJ2501()
