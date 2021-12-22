# 1 1
# 1 1 5
# 2 1 2 5
# 2 1 2 5 10
# 2 -99 1 2 5 10
# 2 -99 1 2 5 7 10
# 5 -99 1 2 5 5 7 10
import heapq
import sys

def BOJ1655():
  n = int(sys.stdin.readline())
  l = heapq.heapify([])
  num = int(sys.stdin.readline())
  l = heapq.heappush(l, num)
  s = heapq.heappop(l)
  print(s)
  heapq.heappush(l, s)
  
  for i in range(n-1) :
    heapq.heappush(l, int(sys.stdin.readline()))
    
    print(l[len(l) // 2])

BOJ1655()
