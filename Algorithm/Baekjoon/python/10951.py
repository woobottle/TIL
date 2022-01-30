import sys
input = sys.stdin.readline

def BOJ10951() :
  while True:
    try :
      a, b = map(int, input().split())
      print(a + b)
    except :
      return


BOJ10951()
