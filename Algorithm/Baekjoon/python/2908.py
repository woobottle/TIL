import sys
input = sys.stdin.readline

def BOJ2908() :
  a, b = map(list, input().split())
  int_a = int("".join(a[::-1]))
  int_b = int("".join(b[::-1]))
  print(max(int_a, int_b))

BOJ2908()
