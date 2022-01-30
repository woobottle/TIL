import sys
input = sys.stdin.readline

def BOJ2750() :
  N = int(input())
  l = []
  for _ in range(N) :
    l.append(int(input()))
  l.sort()
  for i in l :
    print(i)
BOJ2750()
