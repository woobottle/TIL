import sys
input = sys.stdin.readline


def BOJ10826():
  fibonacci = [0, 1, 1] + [0] * 10000
  for i in range(3, 10003):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

  n = int(input())
  print(fibonacci[n])


BOJ10826()
