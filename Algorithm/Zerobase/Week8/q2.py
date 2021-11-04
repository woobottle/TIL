def solution(N, fry, clean, C) :
  total = []
  for i in range(len(fry)) :
    total.append([fry[i], clean[i], False, False])
  total.sort(key=lambda x : (x[0] + x[1], x[0]))
  
  answer = 0
  while (C != 0) :
    answer += 1
    for i in range(len(total)) :
      [fry, clean, is_working, is_cool] = i
      if C == 0 : 
        break
      if not is_working :
        i[2] = True
      if not is_cool :
        i[3] = True
        C -= 1
  
  return answer

print(solution(2, [3, 6], [2, 1], 20)) # 58
print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))  # 2