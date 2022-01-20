import sys 
input = sys.stdin.readline

def BOJ11653() :
  N = int(input())
  while N != 1 :
    for i in range(2, N+1) :
      if N % i == 0 :
        print(i)
        N //= i
        break

BOJ11653()