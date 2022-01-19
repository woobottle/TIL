import sys
input = sys.stdin.readline

def BOJ11399() :
  N = int(input())
  times = list(map(int, input().split()))
  times.sort()
  result = [0 for _ in range(N)]
  result[0] = times[0]
  for i in range(1, len(times)) :
    result[i] = result[i-1] + times[i]
  print(sum(result))

BOJ11399()