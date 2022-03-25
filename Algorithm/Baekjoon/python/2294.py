# 동전의 최소 개수
import sys
input = sys.stdin.readline

def BOJ2294() :
  n, k = map(int, input().split())
  coins = []
  for _ in range(n) :
    coins.append(int(input().strip()))

  dp = [1e6 for _ in range(k+1)]
  dp[0] = 0

  for i in range(1, k + 1) :
    for coin in coins :
      if i - coin >= 0 :
        dp[i] = min(dp[i], dp[i-coin] + 1)

  if dp[-1] == 1e6 :
    print(-1)
  else :
    print(dp[-1])
BOJ2294()

# 12 1 1 1
# 5 5 5