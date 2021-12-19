## 리스트 크기를 n으로 유지하고 입력값들을 거기에 맞게 들어가게 하자
## 들어갈때마다 순서가 정렬되어야 한다.

import sys, heapq

def BOJ2075(): 
  n = int(input())
  array = list(map(int, sys.stdin.readline().split()))
  for _ in range(n-1) :
    for i in list(map(int, sys.stdin.readline().split())):
      if array[0] < i :
        heapq.heappop(array)
        heapq.heappush(array, i)
    
  print(array[0])

BOJ2075()
