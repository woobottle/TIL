import sys
input = sys.stdin.readline

def BOJ11055() :
  n = int(input())
  l = list(map(int, input().split()))
  dp = list(l)

  for i in range(1, n) :
    for j in range(i) :
      if l[i] > l[j] :
        dp[i] = max(dp[i], dp[j] + l[i])

  print(max(dp))

BOJ11055()
