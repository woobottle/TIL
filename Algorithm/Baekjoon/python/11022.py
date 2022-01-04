import sys
input = sys.stdin.readline

def BOJ11022():
  T = int(input())
  for i in range(T):
    A, B = map(int, input().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")

BOJ11022()
