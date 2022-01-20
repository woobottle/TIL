import sys
input = sys.stdin.readline

def BOJ10817() :
  l = list(map(int, input().split()))
  l.sort()
  print(l[1])

BOJ10817()