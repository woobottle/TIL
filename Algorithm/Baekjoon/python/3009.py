import sys
input = sys.stdin.readline

def BOJ3009() :
  x = {}
  y = {}
  for _ in range(3) :
    a, b = map(int, input().split())
    
    if a in x.keys() :
      x[a] += 1
    else :
      x[a] = 1

    if b in y.keys():
      y[b] += 1
    else:
      y[b] = 1

  result_x = 0
  result_y = 0

  for key, value in x.items() :
    if value == 1 :
      result_x = key

  for key, value in y.items():
    if value == 1:
      result_y = key

  print(f'{result_x} {result_y}')
  
BOJ3009()
