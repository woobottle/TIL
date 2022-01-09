import sys 
input = sys.stdin.readline

def BOJ10871() :
  N, X = map(int, input().split())
  A = list(map(int, input().split()))
  print(*list(filter(lambda x : x < X, A)))

BOJ10871()