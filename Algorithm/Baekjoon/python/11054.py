import sys
input = sys.stdin.readline

def BOJ11054() :
  n = int(input())
  l = list(map(int, input().split()))

  dp_up = [1 for _ in range(n)]
  dp_down = [1 for _ in range(n)]

  for i in range(n) :
    for j in range(i) :
      if l[i] > l[j] :
        dp_up[i] = max(dp_up[i], dp_up[j]+1)

  for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
      if l[i] > l[j]:
        dp_down[i] = max(dp_down[i], dp_down[j]+1)

  dp = []
  for up, down in zip(dp_up, dp_down) :
    dp.append(up + down - 1)
  
  print(max(dp))
  
BOJ11054()
