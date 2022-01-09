import sys
input = sys.stdin.readline

def BOJ10950() :
  T = int(input())
  for _ in range(T) :
    A, B = map(int, input().split())
    print(A + B)

BOJ10950()