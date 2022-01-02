import sys
from bisect import bisect_left
input = sys.stdin.readline


def BOJ12738():
  N = int(input())
  A = list(map(int, input().split()))

  dist = [-1000000001]
  index = [0] * (N + 1)

  for i in range(len(A)):
    num = A[i]
    if dist[-1] < num:
      dist.append(num)
    else:
      index[i] = bisect_left(dist, num)
      dist[index[i]] = num

  max_length = len(dist) - 1
  print(max_length)


BOJ12738()
