import sys
input = sys.stdin.readline

def BOJ2530() :
  A, B, C = map(int, input().split())
  D = int(input())
  up_minute, remain_second = divmod(C+D, 60)
  up_time, remain_minute = divmod(B+up_minute, 60)
  print((A+up_time) % 24, remain_minute, remain_second) 

BOJ2530()