import string

def BOJ1935() :
  n = int(input())
  quest = input()
  numbers = {}
  for i in string.ascii_uppercase[:n] :
    numbers[i] = float(input())

  stack = []
  ord = {'+': 1, '-': 1, '*': 2, '/': 2}
  for s in list(quest) :
    if s in ord :
      second = stack.pop()
      first = stack.pop()
      temp = 0
      if s == '+' :
        temp = first + second
      elif s == '-' :
        temp = first - second
      elif s == '*':
        temp = first * second
      elif s == '/':
        temp = first / second
      stack.append(temp)
    else :
      stack.append(numbers[s])
  
  print("{:.2f}".format(stack[-1]))


BOJ1935()
