import sys
input = sys.stdin.readline

def BOJ2588():
  A = int(input())
  B = int(input())
  for i in reversed(list(str(B))) :
    print(A * int(i))
  print(A*B)

BOJ2588()
