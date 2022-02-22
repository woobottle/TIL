import sys
input = sys.stdin.readline

def BOJ2629() :
  n = int(input())
  weight = list(map(int, input().split()))
  input()
  need_check = list(map(int, input().split()))

  dp = [[0 for _ in range(40001)] for _ in range(n)] 
  dp[0][weight[0]] = 1

  for i in range(1, n) :
    dp[i][weight[i]] = 1 

    for j in range(40001) :
      if dp[i-1][j] == 1 :
        dp[i][j] = 1
        dp[i][j + weight[i]] = 1
        dp[i][abs(j - weight[i])] = 1

  for i in need_check :
    if dp[n-1][i] :
      print("Y", end = " ")
    else :
      print("N", end = " ")

BOJ2629()
