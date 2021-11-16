n = int(input())
l = [1000000] * (2000000)
l[0] = 0
l[1] = 0

for i in range(2, 1000001) :
  if i % 6 == 0 :
    l[i] = min(l[i], l[i//2] + 1, l[i//3] + 1)
  if i % 3 == 0 :
    l[i] = min(l[i], l[i//3] + 1)
  if i % 2 == 0 :
    l[i] = min(l[i], l[i//2] + 1)
  l[i] = min(l[i], l[i-1] + 1)

print(l[n])
