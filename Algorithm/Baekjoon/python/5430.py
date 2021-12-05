t = int(input())

def func(x) :
  if x != '' :
    return int(x)
  
for _ in range(t) :
  commands = list(input())
  n = input()
  array = list(filter(lambda x : x != None, list(map(func, input().replace('[', '').replace(']', '').split(',')))))
  flag = True
  reverse_count = 0
  for cmd in commands :
    if cmd == 'R' :
      reverse_count += 1
    elif cmd == 'D' :
      if len(array) == 0 :
        flag = False
        break
      else :
        if reverse_count % 2 == 1 :
          array.pop()
        else :
          array.pop(0)
  
  if flag :
    if reverse_count % 2 == 1 :
      array.reverse()
    # print(array)
    if len(array) != 0 :
      print("[" + ",".join(list(map(str, array))) + "]")
    else :
      print("[]")
  else :
    print('error')
