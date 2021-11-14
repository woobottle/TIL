def solution(N, fry, clean, C) :
  left = 0
  right = C * max([x + y for x,y in zip(fry, clean)])
  answer = right

  while left <= right :
    mid = (left + right) // 2
    
    val = 0
    for f,c in zip(fry, clean) :
      val += (mid + c) // (f + c)
    
    if val >= C :
      right = mid - 1
      answer = min(answer, mid)
    else :
      left = mid + 1


  return answer

print(solution(2, [3, 6], [2, 1], 20)) # 58
print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))  # 2

