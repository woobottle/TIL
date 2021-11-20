tc = int(input())

for _ in range(tc) : 
  n, m = list(map(int, input().split()))
  array = list(map(int, input().split()))
  index = list(range(len(array)))
  index[m] = 'target'
  order = 0
  
  while True :
    if array[0] == max(array) :
      order += 1
      if index[0] == 'target' :
        print(order)
        break
      else :
        array.pop(0)
        index.pop(0)

    else :
      index.append(index.pop(0))
      array.append(array.pop(0))
