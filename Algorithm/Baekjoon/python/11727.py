import sys
input = sys.stdin.readline
mod_num = 10_007

def BOJ11727() :
  n = int(input())
  dp = [0 for _ in range(1001)]
  dp[1] = 1
  dp[2] = 3
  for i in range(3, 1001) :
    dp[i] = ((dp[i-2] * 2) % mod_num + (dp[i-1]) % mod_num) % mod_num
  
  print(dp[n])

BOJ11727()
