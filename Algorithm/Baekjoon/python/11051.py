import sys
input = sys.stdin.readline


def BOJ11051():
  N, K = map(int, input().split())
  array = [[0] * (N+1) for _ in range(N+1)]

  for i in range(N+1):
    for j in range(N+1):
      if j == 1:
        array[i][j] = i
      elif i == j:
        array[i][j] = 1
      elif i < j:
        break
      else:
        array[i][j] = ((array[i-1][j-1] % 10007) +
                       (array[i-1][j] % 10007)) % 10007

  print(array[N][K])


BOJ11051()
