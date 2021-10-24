def divide_by_two(num) :
  body = 0
  while (num) :
    body += num // 2
    num //= 2
  return body

def divide_by_five(num) :
  body = 0
  while (num):
    body += num // 5
    num //= 5
  return body

n, m = map(int, input().split())

count_five = divide_by_five(n) - divide_by_five(m) - divide_by_five(n - m)
count_two = divide_by_two(n) - divide_by_two(m) - divide_by_two(n - m)

print(min(count_five, count_two))
