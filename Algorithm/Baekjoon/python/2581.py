MAX_NUM = 10001
import sys
import math
input = sys.stdin.readline

def BOJ2581() :
  array = [False for _ in range(MAX_NUM)]
  array[1] = True
  
  for i in range(2, int(math.sqrt(MAX_NUM))) :
    for j in range(i*2, MAX_NUM, i) :
      if array[j] == False :
        array[j] = True

  M = int(input())
  N = int(input())

  if False not in array[M:N+1] :
    print(-1)
    return
  
  total = 0
  min = 0
  for i in range(M, N+1) :
    if min == 0 and array[i] == False :
      min = i
    
    if array[i] == False :
      total += i
  
  print(total)
  print(min)

BOJ2581()
