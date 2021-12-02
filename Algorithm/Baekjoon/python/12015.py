import sys
from bisect import bisect_left

def find(target):
  start, end = 1, len(dist) - 1
  while start < end :
    mid = (start + end) // 2
    if dist[mid] < target :
      start = mid + 1
    elif dist[mid] > target :
      end = mid
    else :
      start = end = mid
  return end


n = int(input())
array = list(map(int, sys.stdin.readline().split()))
dist = [0]

for i in array :
  if dist[-1] < i :
    dist.append(i)
  else :
    dist[find(i)] = i
    # dist[bisect_left(dist, i)] = i

print(len(dist) - 1)
