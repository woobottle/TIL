import sys
input = sys.stdin.readline

def BOJ2476() :

  def get_result(a, b, c) :
    result = 0
    if a == b == c:
      result = 10000 + a * 1000
    elif a == b:
      result = 1000 + a * 100
    elif a == c:
      result = 1000 + a * 100
    elif b == c:
      result = 1000 + b * 100
    else:
      result = max(a, b, c) * 100
    return result

  N = int(input())
  answer = 0 
  for _ in range(N) :
    a, b, c = map(int, input().split())
    answer = max(answer, get_result(a, b, c))
  print(answer)

BOJ2476()
