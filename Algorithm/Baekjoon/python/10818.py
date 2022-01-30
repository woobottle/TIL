import sys
input = sys.stdin.readline

def BOJ10818() :
  int(input())
  l1 = list(map(int, input().split()))
  print(min(l1), max(l1))

BOJ10818()
