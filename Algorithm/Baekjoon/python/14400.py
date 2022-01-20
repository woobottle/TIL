import sys
input = sys.stdin.readline

def BOJ14400():
  n = int(input())
  l = []
  a = []
  b = []
  for _ in range(n) :
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    l.append([x,y])
  a.sort()
  b.sort()
  x_median = a[len(a)//2]
  y_median = b[len(b)//2]
  
  result = 0
  for x, y in l :
    result += abs(x-x_median) + abs(y-y_median)
  print(result)
BOJ14400()
