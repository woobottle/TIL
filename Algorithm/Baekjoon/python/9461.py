import sys 
input = sys.stdin.readline

def BOJ9461() :
  T = int(input())
  dp = [0] * 102
  dp[0] = 1
  dp[1] = 1
  dp[2] = 1
  for i in range(3, 102) :
    dp[i] = dp[i-3] + dp[i-2]


  for _ in range(T) :
    n = int(input())
    print(dp[n-1])

BOJ9461()