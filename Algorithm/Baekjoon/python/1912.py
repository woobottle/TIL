import sys
input = sys.stdin.readline

def BOJ1912() :
  n = int(input())
  l = list(map(int, input().split()))
  dp = list(l)
  for i in range(1, n) :
    dp[i] = max(dp[i-1] + l[i], l[i])

  print(max(dp))

BOJ1912()
