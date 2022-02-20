import sys
input = sys.stdin.readline
mod_num = 10_007

def BOJ11057() :
  n = int(input())
  dp = [[0 for _ in range(10)] for _ in range(n+1)]
  dp[1] = [1 for _ in range(10)]
  
  for i in range(2, n+1) :
    for j in range(10) :
      dp[i][j] = sum(dp[i-1][:j+1]) % mod_num
  
  print(sum(dp[n]) % mod_num)

BOJ11057()
