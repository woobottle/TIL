import sys
input = sys.stdin.readline

def BOJ2739() :
  N = int(input())
  for i in range(1, 10) :
    print(f"{N} * {i} = {N*i}")

BOJ2739()