def BOJ1316() :
  n = int(input())
  count = 0
  for _ in range(n) :
    pointer = ''
    dict = {}
    flag = True
    for k in list(input()) :
      if pointer != k and k not in dict :
        pointer = k
        dict[k] = 1
      elif pointer == k and k in dict :
        continue
      elif pointer != k and k in dict :
        flag = False
        break
    if flag :
      count += 1
  print(count)

BOJ1316()