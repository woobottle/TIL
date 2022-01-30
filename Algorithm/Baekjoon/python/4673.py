import sys
input = sys.stdin.readline

def BOJ4673() :
  def generate_number(n) :
    sum = n
    for i in list(str(n)) :
      sum += int(i)
    
    return sum

  l = [0 for _ in range(10001)]
  
  for i in range(1, 10000) :
    temp = i
    while True :
      temp = generate_number(temp)
      if temp < 10001 :
        l[temp] = 1
      else :
        break

  for i in range(1, len(l)) :
    if l[i] == 0 :
      print(i)

BOJ4673()
