n = int(input())
array = []
for i in range(n) :
  array.append(int(input()))

number = 1
count = 1
answer = []
stack = []

for i in array :
  while count <= i :
    stack.append(number)
    number += 1
    count += 1
    answer.append('+')
  if stack[len(stack) - 1] == i :
    stack.pop()
    answer.append('-')
  else :
    answer = 'NO'
    break
  
if answer == "NO" :
  print(answer)
else :
  print('\n'.join(answer))