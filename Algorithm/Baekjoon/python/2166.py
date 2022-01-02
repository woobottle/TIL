from itertools import combinations
import sys 
import math
input = sys.stdin.readline

def BOJ2166() :
  N = int(input())
  x_points = []
  y_points = []
  
  for _ in range(N) :
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

  result = 0
  for i in range(N) :
    if i == N-1 :
      result += x_points[i] * y_points[0]
    else :
      result += x_points[i] * y_points[i+1]

  for i in range(N):
    if i == N-1 :
      result -= x_points[0] * y_points[i]
    else :
      result -= x_points[i+1] * y_points[i]

  print(math.floor((abs(result) * 0.5 * 10) + 0.5) / 10)

BOJ2166()

# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
