import math
import sys
input = sys.stdin.readline

def BOJ1978() :
  array = [False for _ in range(1001)]
  for i in range(2, int(math.sqrt(1001))) :
    for j in range(i*2, 1001, i) :
      if array[j] == False :
        array[j] = True
  array[1] = True
  
  N = int(input())
  answer = 0
  l = list(map(int, input().split()))
  for i in l :
    if array[i] == False :
      answer += 1
  print(answer)

BOJ1978()
