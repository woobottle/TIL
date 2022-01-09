import sys
input = sys.stdin.readline

def BOJ2439() :
  N = int(input())
  for i in range(1, N+1) :
    for _ in range(N - i):
      print(" ", end='')
    for _ in range(i) :
      print("*", end = '')
    print()

BOJ2439()
