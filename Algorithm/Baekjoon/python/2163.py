import sys
input = sys.stdin.readline

def BOJ2163() :
  N, M = map(int, input().split())
  print(N*M - 1)

BOJ2163()