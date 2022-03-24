# import sys
# input = sys.stdin.readline

# def BOJ2293() :
#   n, k = map(int, input().split())
#   l = []
#   for _ in range(n) :
#     l.append(int(input()))

#   dp = [0 for _ in range(k+1)]
#   dp[0] = 1

#   for i in l :
#     for j in range(1, k+1) :
#       if j - i >= 0 :
#         dp[j] += dp[j-i]
  
#   print(dp[-1])
  
# BOJ2293()


import sys 
input = sys.stdin.readline

def BOJ2293() :
  n, k = map(int, input().split())
  dp = [0 for _ in range(k+1)]
  dp[0] = 1
  coins = []

  for _ in range(n) :
    input_num = int(input().strip())
    coins.append(input_num)
    
  for i in coins :
    for j in range(1, k+1) :
      if j - i >= 0 :
        dp[j] += dp[j-i]

  print(dp[-1])

BOJ2293()

