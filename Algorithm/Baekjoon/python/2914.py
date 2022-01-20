import sys
input = sys.stdin.readline

def BOJ2914() :
  A, I = map(int, input().split())
  print(A * (I-1) + 1)

BOJ2914()