import sys
input = sys.stdin.readline
mod_num = 1_000_000_000

def BOJ10844() :
  n = int(input())
  dp = [[0 for _ in range(10)] for _ in range(101)]
  dp[1] = [0] + [1 for _ in range(9)]
  
  for i in range(2, 101) :
    for j in range(10) :
      if j == 0 :
        dp[i][j] = dp[i-1][1] % mod_num
      elif j == 9 :
        dp[i][j] = dp[i-1][8] % mod_num
      else :
        dp[i][j] = (dp[i-1][j-1] % mod_num + dp[i-1][j+1] % mod_num) % mod_num

  print(sum(dp[n]) % mod_num)

BOJ10844()
