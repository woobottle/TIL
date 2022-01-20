import sys
input = sys.stdin.readline

def BOJ2935() :
  A = int(input())
  operator = input().rstrip()
  B = int(input())

  if operator == "*" :
    print(A * B)
  else :
    print(A + B)

BOJ2935()