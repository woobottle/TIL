def BOJ1107(): 
  n = int(input())
  m = int(input())
  count = abs(100 - n)
  button = [True] * 10
  if m != 0 :
    for errored in list(map(int, input().split())) :
      button[errored] = False
  
  for i in range(1000001) :
    listed_number = list(str(i))
    listed_number_length = len(listed_number)
    flag = True
    for number in listed_number : 
      if button[int(number)] == False :
        flag = False
        break
    if flag : 
      count = min(count, listed_number_length + abs(n - i))
  print(count)

BOJ1107()
