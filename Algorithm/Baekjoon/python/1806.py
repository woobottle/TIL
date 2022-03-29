# import sys
# input = sys.stdin.readline

# def BOJ1806() :
#   N, S = map(int, input().split())
#   l = list(map(int, input().split()))

#   f_p = 1
#   s_p = 0
#   result = 1e10

#   s = [0, l[0]]
#   for i in range(1, len(l)) :
#     s.append(l[i] + s[i])

#   if S > s[-1]:
#     print(0)
#     return

#   while f_p <= N and s_p <= N :
#     if s[f_p] - s[s_p] >= S :
#       result = min(result, f_p - s_p)
#       s_p += 1
#       if f_p == s_p :
#         f_p += 1
#     else :
#       f_p += 1

#   print(result)

# BOJ1806()


import sys
input = sys.stdin.readline

def BOJ1806() :
  N, S = map(int, input().split())
  numbers = list(map(int, input().split()))
  first_pointer = 0
  second_pointer = 1

  if sum(numbers) < S :
    print(0)
    return

  remains = [0]
  for i in range(len(numbers)) :
    next_remain = remains[i] + numbers[i]
    remains.append(next_remain)

  min_length = 1e6
  while first_pointer < second_pointer and first_pointer <= N and second_pointer <= N :
    partition_remains = remains[second_pointer] - remains[first_pointer]
    if partition_remains < S:
      second_pointer += 1
      continue
    
    if partition_remains >= S :
      min_length = min(min_length, second_pointer - first_pointer)
      first_pointer += 1
      if first_pointer == second_pointer :
        second_pointer += 1
      continue

  print(min_length)

BOJ1806()
