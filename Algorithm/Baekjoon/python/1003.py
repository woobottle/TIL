import sys 
input = sys.stdin.readline

def BOJ1003() :
  T = int(input())
  dp = [0] * 41
  dp[0] = [1, 0]
  dp[1] = [0, 1]
  dp[2] = [1, 1]

  for i in range(3, 41) :
    temp = []
    for a, b in zip(dp[i-1], dp[i-2]) :
      temp.append(a+b)
    dp[i] = temp

  for i in range(T) :
    print(*dp[int(input())])
  

BOJ1003()
