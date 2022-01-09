import sys
input = sys.stdin.readline


def BOJ11402():
  N, K, prime = map(int, input().split())
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
  print(factorial(N))
  print(factorial(N-K))
  print(factorial(K))
  print((factorial(N) % prime * pow(factorial(K) * factorial(N-K), prime - 2)) % prime)


BOJ11402()
