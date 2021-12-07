def gcd(first, second) :
  array = [0] * (first + 1)
  for i in range(1, first+1) :
    if first % i == 0 :
      array[i] = 1
  
  max_num = 0
  for i in range(len(array)):
    if array[i] == 1 and second % i == 0:
      max_num = i
  
  return max_num

t = int(input())

for _ in range(t) :
  a,b = map(int, input().split())
  print((a*b) // gcd(a,b))


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)


t = int(input())
while t:
  a, b = map(int, input().split())
  print(a*b//gcd(a, b))
  t -= 1
