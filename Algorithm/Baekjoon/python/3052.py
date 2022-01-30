import sys
input = sys.stdin.readline

def BOJ3052() :
  l = []
  for _ in range(10) :
    l.append(int(input()))

  dict = {}
  for i in l :
    key = i % 42
    if key in dict.keys() :
      dict[key] += 1
    else :
      dict[key] = 0

  print(len(dict.keys()))
BOJ3052()
