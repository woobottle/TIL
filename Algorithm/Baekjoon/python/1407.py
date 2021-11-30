a,b = map(int, input().split())

def calc(number) :
  i = 1
  count = 0
  x = number
  while x > 0 :
    if x % 2 != 0 :
      y = x // 2 + 1
    else :
      y = x // 2
    count += y * i
    i *= 2
    x -= y
    
  return count

print(calc(b) - calc(a-1))
