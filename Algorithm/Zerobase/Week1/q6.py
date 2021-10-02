a = ['파', '이', '썬', '썬', '썬', '썬', '즐', '즐', '즐', '거', '운']
last = None
for elem in a :
  if elem == last :
    continue
  print(elem, end='')
  last = elem