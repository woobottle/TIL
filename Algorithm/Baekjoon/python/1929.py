m, n = map(int, input().split())

max_value = 1000001
array = [0] * max_value
array[0] = 1
array[1] = 1
array[2] = 0

for i in range(2, max_value) :
  for j in range(i*i, max_value, i) :
    if array[j] == 0 :
      array[j] = 1

result = []
for i in range(m, n + 1) :
  if array[i] == 0 :
    result.append(i)

for i in result :
  print(i)