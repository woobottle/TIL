def solution(numbers) :
  ls = sorted(list(map(lambda x: str(x), numbers)), reverse=True, key=lambda x : x.ljust(4, '0'))
  return "".join(ls)


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9])) # 9534330
