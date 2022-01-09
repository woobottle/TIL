import sys 
input = sys.stdin.readline

def BOJ8393() :
  N = int(input())
  ans = 0
  for i in range(N+1) :
    ans += i
  print(ans)

BOJ8393()