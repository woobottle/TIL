# import re

# s = "one2three4five6"
# print(list(re.split('(\d)', s)))

# print(list(filter(lambda x: x != '', list(re.split('(\d)', s)))))


def func(x) :
  if x > 0 :
    return True
  else :
    return False

array = [-2, -1, 0, 1, 2]
print(list(filter(func, array)))
print(list(filter(lambda x: x > 0, array)))
