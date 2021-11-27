import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for i in range(n) :
  num = int(sys.stdin.readline())
  if num == 0 and len(heap) == 0:
    print(0)
  elif num == 0 :
    print(heapq.heappop(heap)[1])
  else :
    heapq.heappush(heap, (-num, num))
