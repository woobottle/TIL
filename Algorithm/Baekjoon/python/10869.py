import sys
input = sys.stdin.readline

def BOJ10869() :
  A,B = map(int, input().split())
  print(A+B)
  print(A-B)
  print(A*B)
  print(A//B)
  print(A%B)

BOJ10869()
