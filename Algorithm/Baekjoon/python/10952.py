import sys
input = sys.stdin.readline

def BOJ10952() :
  while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
      break
    print(a + b)

BOJ10952()
