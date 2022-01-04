import sys
input = sys.stdin.readline


def BOJ2748():
  fibonacci = [0, 1, 1] + [0] * 96
  for i in range(3, 96):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

  n = int(input())
  print(fibonacci[n])


BOJ2748()
