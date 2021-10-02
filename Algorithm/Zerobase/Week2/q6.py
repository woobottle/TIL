def init_sum(*args):
  try:
    for n in args:
      sum += n
  except:
    print('error')
  return sum

print(init_sum('1', '2'))