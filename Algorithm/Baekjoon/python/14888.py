INF = 1e9
from itertools import permutations
import sys
input = sys.stdin.readline

def BOJ14888() :
  def calculate(list_of_operator, list_of_number) :
    result = list_of_number[0]
    for op, num in zip(list_of_operator, list_of_number[1:]) :
      if op == '+' :
        result += num
      if op == '-' :
        result -= num
      if op == '*':
        result *= num
      if op == '/':
        if result > 0 :
          result //= num
        else :
          result = ((result * (-1)) // num) * (-1)
    
    return result

  N = int(input())
  numbers = list(map(int, input().split()))
  add, sub, mul, div = list(map(int, input().split()))
  operators = ['+' for _ in range(add)] + ['-' for _ in range(sub)] + ['*' for _ in range(mul)] + ['/' for _ in range(div)]

  maximum = -INF
  minimum = INF

  for operator in list(permutations(operators)) :
    total = calculate(operator, numbers)
    if total > maximum :
      maximum = total
    if total < minimum :
      minimum = total

  print(maximum)
  print(minimum)

BOJ14888()
