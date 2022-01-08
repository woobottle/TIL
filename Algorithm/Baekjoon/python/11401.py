import sys
input = sys.stdin.readline

def BOJ11401() :
  def factorial(n) :
    ans = 1
    for i in range(1, n+1) :
      ans *= i
    return ans

  def pow(a, b) :
    if b == 1 :
      return a 
    elif b % 2 == 0 :
      return pow(a, b//2) ** 2
    else :
      return pow(a, b//2) * a ** 2

  N, K = map(int, input().split())
  array = [[0] * (N+1) for _ in range(N+1)]
  
  
  
  
BOJ11401()
