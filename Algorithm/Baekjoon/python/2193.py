import sys
input = sys.stdin.readline

def BOJ2193() :
  n = int(input())
  dp = [[0 ,0] for _ in range(91)]
  dp[1] = [0, 1]
  dp[2] = [1, 0]
  for i in range(3, 91) :
    dp[i] = [sum(dp[i-1]), dp[i-1][0]]

  print(sum(dp[n]))

BOJ2193()


# 1
# 10
# 100, 101
# 1001, 1000, 1010
