import sys
input = sys.stdin.readline

def BOJ11720() :
  n = int(input())
  l = list(map(int, list(input().rstrip())))
  print(sum(l))

BOJ11720()
