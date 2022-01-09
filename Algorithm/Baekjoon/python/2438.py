import sys 
input = sys.stdin.readline

def BOJ2438() :
  N = int(input())
  for i in range(1, N+1) :
    for _ in range(i) :
      print('*', end = '')
    print()

BOJ2438()
