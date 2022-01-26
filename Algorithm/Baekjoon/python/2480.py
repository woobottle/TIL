import sys
input = sys.stdin.readline

def BOJ2480() :
  a, b, c = map(int, input().split())
  result = 0
  if a == b == c :
    result = 10000 + a * 1000
  elif a == b :
    result = 1000 + a * 100
  elif a == c :
    result = 1000 + a * 100
  elif b == c :
    result = 1000 + b * 100
  else :
    result = max(a,b,c) * 100

  print(result)  

BOJ2480()
