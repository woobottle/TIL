import sys 
input = sys.stdin.readline

def BOJ2675() :
  T = int(input())
  for _ in range(T) :
    R, S = input().split()
    for i in list(S) :
      for _ in range(int(R)) :
        print(i, end = "")
    print()

BOJ2675()