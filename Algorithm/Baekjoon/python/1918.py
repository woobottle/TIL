n = list(input())

operator = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
result = ""
stack = []

for i in n :
  if i == '(' :
    stack.append(i)
  elif i == ')' :
    top = stack.pop()
    while stack and top != '(' :
      result += top
      top = stack.pop()

  elif i in operator :
    while stack and operator[stack[len(stack) - 1]] >= operator[i] :
      top = stack.pop()
      if i != '(' :
        result += top
    stack.append(i)
  else :
    result += i

while len(stack) != 0 :
  result += stack.pop()

print(result)
