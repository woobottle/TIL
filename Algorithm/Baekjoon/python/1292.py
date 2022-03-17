import sys
input = sys.stdin.readline

def BOJ1292() :
  A, B = map(int, input().split())
  l = [1]
  count = 1
  start = 2
  flag = False
  while True :  
    for _ in range(start) :
      l.append(start)
      count += 1
      if count == 1001 :
        flag = True
    if flag :
      break
    start += 1
  
  print(sum(l[A-1:B]))

BOJ1292()
