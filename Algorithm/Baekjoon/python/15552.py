import sys
input = sys.stdin.readline

def BOJ15552() :
  T = int(input())
  for _ in range(T) :
    a, b = map(int, input().split())
    print(a + b)

BOJ15552()
