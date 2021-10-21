def solution(n, k):
  arr = list(range(1, n))
  used = [0 for _ in range(n + 1)]
  result = []

  def get_all_list(elements, used) :
    if (len(elements) == n) :
      result.append(elements[:])
      return
    
    for i in range(1, n+1) :
      if not used[i] :
        elements.append(i)
        used[i] = 1
        get_all_list(elements, used)
        used[i] = 0
        elements.pop()
  get_all_list([], used)

  return result[k-1]

print(solution(3,3)) # [2, 1, 3]
print(solution(4,9)) # [2, 3, 1, 4]


