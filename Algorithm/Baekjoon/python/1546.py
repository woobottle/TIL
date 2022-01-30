import sys
input = sys.stdin.readline

def BOJ1546() :
  N = int(input())
  l = list(map(int, input().split()))
  max_num = max(l)

  temp = list(map(lambda x : x / max_num * 100, l))
  print(sum(temp) / len(temp))

BOJ1546()
