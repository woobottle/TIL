import sys
input = sys.stdin.readline

def BOJ10430() : 
  A,B,C = map(int, input().split())
  print((A+B)%C)
  print(((A % C) + (B % C)) % C)
  print((A*B)%C)
  print(((A % C) * (B % C)) % C)

BOJ10430()
