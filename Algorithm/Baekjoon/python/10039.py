import sys 
input = sys.stdin.readline

def BOJ10039() :
  sum = 0
  for _ in range(5) :
    temp = int(input())
    if temp < 40 :
      temp = 40
    sum += temp
  print(sum//5)
BOJ10039()
