def get_c(x, y, width) :
  h1 = (x**2 - width**2)**0.5
  h2 = (y**2 - width**2)**0.5
  c = h1 * h2 / (h1 + h2)
  return c

def BOJ2022() :
  x, y, c = map(float, input().split())
  start, end = 0, min(x,y)
  res = 0
  while (end - start) > 0.000001 :
    width = (start + end) / 2
    res = width
    if get_c(x, y, width) >= c : # c를 구했는데 기존의 c보다 같거나 크면 w값을 키워주어서 h1, h2의 값을 작게 해주어야 한다.
      start = width
    else :
      end = width  
  print(res)

BOJ2022()

# https://jinho-study.tistory.com/687
