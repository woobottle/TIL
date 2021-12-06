n = int(input())

array = []
for i in range(n) :
  n = int(input())
  array.append((n, i))

sorted_array = sorted(array)

answer = 0
for i in range(n) :
  answer = max(answer, sorted_array[i][1] - i + 1)

print(answer) 