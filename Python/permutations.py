from itertools import permutations
from itertools import combinations

a = [1,2,3]

print(list(permutations(a, 2)))
print(list(combinations(a, 2)))

# def permute(array) :
#   result = [array[:]]
#   temp = [0 for _ in range(len(array))]
#   index = 0
#   while index < len(array) :
#     if temp[index] < index :
#       if index % 2 == 0 :
#         array[index], array[0] = array[0], array[index]
#       else :
#         array[temp[index]], array[index] = array[index], array[temp[index]]
#       result.append(array[:])
#       temp[index] += 1
#       index = 0
#     else :
#       temp[index] = 0
#       index += 1

  # return result


def permute(array, r) :
  used = [False for _ in range(len(array))]
  result = []
  
  def generate(arr, used) :
    if len(arr) == r :
      result.append(arr[:])
      return
    
    for i in range(len(array)) :
      if not used[i] :
        arr.append(array[i])
        used[i] = True
        generate(arr, used)
        used[i] = False
        arr.pop()

  generate([], used)
  return result

def combinated(array, r) :
  used = [False for _ in range(len(array))]
  result = []
  
  def generate(arr) :
    if len(arr) == r and sorted(arr[:]) not in result :
      result.append(arr[:])
      return

    for i in range(len(array)) :
      if not used[i] :
        arr.append(array[i])
        used[i] = True
        generate(arr)
        used[i] = False
        arr.pop()

  generate([])
  return result

print(permute(a, 2))
print(combinated(a, 2))

# 출처 https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0