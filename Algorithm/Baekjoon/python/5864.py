import sys
input = sys.stdin.readline
INF = 1e11


def BOJ5864():
  N, A, B = map(int, input().split())
  dp = [INF for _ in range(1000001)]
  cows = []
  for _ in range(N):
    curr_cow = int(input())
    cows.append(curr_cow)
  cows.sort()

  curr_wifi = cows[0]
  dp[curr_wifi] = A
  for i in range(1, len(cows)):
    dp[cows[i]] = min(dp[cows[i-1]] + B * (cows[i] -
                      cows[i-1]) / 2, dp[cows[i-1]] + A)
  if dp[cows[-1]] % 1 == 0:
    print(int(dp[cows[-1]]))
  else:
    print(dp[cows[-1]])


BOJ5864()
