from itertools import permutations

def calculate(op, num1, num2) :
  result = 0
  if op == '*' :
    result = int(num1) * int(num2)
  if op == '+' :
    result = int(num1) + int(num2)
  if op == '-' :
    result = int(num1) - int(num2)
  return result

def solution(expression) :
  temp = []
  result = []
  last_index = 0
  has = set()
  
  for i in range(len(expression)) :
    if expression[i] in ['*', '+', '-'] :
      temp.append(expression[last_index:i])
      temp.append(expression[i])
      has.add(expression[i])
      last_index = i + 1
  if last_index != len(expression) :
    temp.append(expression[last_index:])
    last_index = 0
  
  priority_list = list(map(list,permutations([*has], len([*has]))))

  for priority in priority_list :
    l = list(temp)

    for op in priority :
      stack = []
      while (len(l) != 0) :
        tmp = l.pop(0)
        if tmp == op :
          stack.append(calculate(op, stack.pop(), l.pop(0)))
        else :
          stack.append(tmp)
          
      l = stack
    
    result.append(abs(l.pop(0)))
      
  return max(result)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
