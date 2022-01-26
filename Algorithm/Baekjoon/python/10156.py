import sys
input = sys.stdin.readline

def BOJ10156() :
  K, N, M = map(int, input().split())
  result = K * N - M
  if result >= 0 :
    print(result)
  else :
    print(0)

BOJ10156()
