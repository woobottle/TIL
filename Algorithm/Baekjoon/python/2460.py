import sys
input = sys.stdin.readline

def BOJ2460() :
  l = []
  total = 0
  for _ in range(10) :
    a, b = map(int, input().split())
    total = total - a + b
    l.append(total)
  print(max(l))
  
BOJ2460()
