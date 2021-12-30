import sys 
input = sys.stdin.readline

def BOJ1904() :
  dp = [0] * 1000001
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3
  dp[4] = 5
  
  n = int(input())
  for i in range(5, n+1) :
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
  
  print(dp[n])

BOJ1904()