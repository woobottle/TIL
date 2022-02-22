import sys
input = sys.stdin.readline

def BOJ10942() :
  n = int(input())
  l = list(map(int, input().split()))
  m = int(input())
  dp = [[0 for _ in range(n)] for _ in range(n)]

  for diff in range(n) :
    for start in range(n - diff) :
      end = start + diff
      
      if start == end :
        dp[start][end] = 1
        continue
      
      if start + 1 == end :
        if l[start] == l[end] : dp[start][end] = 1
        else :
          dp[start][end] = 0
        continue

      if l[start] == l[end] and dp[start+1][end-1] == 1 :
        dp[start][end] = 1
      else :
        dp[start][end] = 0

  for _ in range(m) :
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

BOJ10942()
