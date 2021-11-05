def solution(N, fry, clean, C) :
  total = []
  for i in range(len(fry)) :
    total.append([fry[i], clean[i], 0])
  total.sort(key=lambda x : (x[0] + x[1], x[0]))
  
  flag = True
  minute = 0
  while (C != 0) :
    for i in range(len(total)) :
      fry, clean, next_run = total[i]
      if next_run == minute :
        total[i][2] = next_run + fry + clean
        C -= 1
        if C == 0 :
          minute += fry
          flag = False
    if flag :
      minute += 1
  
  return minute

print(solution(2, [3, 6], [2, 1], 20)) # 58
print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))  # 2
