k, n = map(int, input().split())
l = []
for i in range(k) :
  l.append(int(input()))

l.sort()
result = 0
left = 1
right = l[len(l) - 1]

while left <= right :
  mid = (left + right) // 2
  
  total = 0
  for i in l :
    total += i // mid
  
  if total >= n :
    result = mid
    left = mid + 1
  elif total < n :
    right = mid - 1
    
print(result)
