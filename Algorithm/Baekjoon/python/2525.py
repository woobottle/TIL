from operator import mod
import sys
input = sys.stdin.readline

def BOJ2525() :
  A, B = map(int, input().split())
  C = int(input())
  up_time, remain_minute = divmod(B+C, 60)
  print((A + up_time) % 24, remain_minute)

BOJ2525()