import sys
input = sys.stdin.readline

def BOJ11021() :
  T = int(input())
  for i in range(T) :
    A,B = map(int, input().split())
    print(f"Case #{i+1}: {A+B}")

BOJ11021()