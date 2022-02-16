# import sys
# input = sys.stdin.readline

# def BOJ2579() :
#   n = int(input())
#   stairs = []
#   for _ in range(n) :
#     stairs.append(int(input()))
  
#   dp = [[0 for _ in range(3)] for _ in range(n + 1)]
#   # dp[i][0] => 해당 칸을 안밟음
#   # dp[i][1] => 해당 칸을 처음 밟음
#   # dp[i][2] => 해당 칸을 연속해서 밟음 (i-1)번째를 밟았음

#   for i in range(1, n+1) :
#     dp[i][0] = max(dp[i-1][1], dp[i-1][2])
#     dp[i][1] = dp[i-1][0] + stairs[i-1]
#     dp[i][2] = dp[i-1][1] + stairs[i-1]
  
#   print(max(dp[n][1], dp[n][2]))

# BOJ2579()

import sys
input = sys.stdin.readline


def BOJ2579():
  n = int(input())
  stairs = [0 for _ in range(301)]
  for i in range(n):
    stairs[i] = int(input())

  dp = [0 for _ in range(301)]
  dp[0] = stairs[0]
  dp[1] = stairs[0] + stairs[1]
  dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

  # 마지막 칸은 꼭 밟아야 한다. 전칸을 밟을 경우와 밟지 않은경우가 있을것이다.
  for i in range(3, n) :
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

  print(dp[n-1])
BOJ2579()
