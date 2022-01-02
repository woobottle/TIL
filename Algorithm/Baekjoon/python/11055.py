import sys
input = sys.stdin.readline

def BOJ11055() :
  N = int(input())
  array = list(map(int, input().split()))
  memo = list(array)
  
  for index in range(1, len(array)) :
    max_point = 0
    for j in range(index) :
      if array[j] < array[index] and max_point < memo[j] + array[index] :
        max_point = memo[j] + array[index]
    memo[index] = max(memo[index], max_point)

  print(max(memo))

BOJ11055()
