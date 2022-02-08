import sys
input = sys.stdin.readline
prime = 1_000_000_007


def BOJ11401():
  def factorial(n):
    ans = 1
    for i in range(1, n+1):
      ans = (ans * i) % prime 
    return ans

  def pow(a, b):
    if b == 1:
      return a
    elif b % 2 == 0:
      return (pow(a, b//2) ** 2) % prime
    else:
      return (pow(a, b//2) ** 2) * a % prime
         
  N, K = map(int, input().split())

  A = factorial(N)
  B = factorial(K) * factorial(N-K)
  print((A % prime * pow(B, prime-2) % prime) % prime)

BOJ11401()
