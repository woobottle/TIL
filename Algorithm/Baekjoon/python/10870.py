import sys
input = sys.stdin.readline


def BOJ10870():
  fibonacci = [0, 1, 1] + [0] * 21
  for i in range(3, 23):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

  n = int(input())
  print(fibonacci[n])


BOJ10870()
