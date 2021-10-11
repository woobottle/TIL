from functools import reduce
def solution(n):
  answer = [];
  is_happy = True
  splitted_int = list(str(n))
  
  while True :
    calculated = reduce(lambda x, y: x + y, map(lambda i : int(i) ** 2, splitted_int)) 
    
    if calculated in answer :
      is_happy = False
      break
    if calculated == 1:
      break

    answer.append(calculated)
    splitted_int = list(str(calculated))

  return is_happy


# Test code
print(solution(100))
print(solution(19))  # True
print(solution(61))  # False
