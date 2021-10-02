import math

for i in range(-1, 11) :
  if i == -1 :
    print(0, end=' ')
  elif i >= 9 :
    print(int(math.pow(2, 8)), end=' ')
  else :
    print(int(math.pow(2,i)), end=' ')