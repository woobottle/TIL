t = int(input())

for i in range(t) :
  stack = []
  target = list(input())
  flag = True
  for s in target :
    if s == '(' :
      stack.append(s)
    else : 
      if len(stack) == 0 :
        flag = False
        break
      else :
        stack.pop()
  
  if len(stack) == 0 and flag:
    print('YES')
  else :
    print('NO')