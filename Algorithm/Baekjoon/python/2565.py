import sys
input = sys.stdin.readline

def BOJ2565() :
  n = int(input())
  l = []
  for _ in range(n) :
    l.append(list(map(int, input().split())))
  
  l.sort()  
  
  dp = [1 for _ in range(n)]
  
  for i in range(n) :
    for j in range(i) :
      if l[j][1] < l[i][1] :
        dp[i] = max(dp[i], dp[j] + 1)
      
  print(n - max(dp))
  

BOJ2565()
