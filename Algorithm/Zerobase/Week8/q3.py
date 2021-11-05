def solution(N, start, end, counts):
  answer = 0
  start = get_N_dimension(N, start)
  for i in counts : 
    if start != get_N_dimension(N, i): 
      answer += 1
    start += 1
  return answer

def get_N_dimension(N, target) :
  number = 0
  index = 1
  num = 0
  target_convert = list(target)
  target_convert.reverse()
  for i in target_convert :
    if i.isalpha() :
      num = get_calculated_num(i)
    else :
      num = int(i)
    number += num * index
    index *= N
  return number

def get_calculated_num(character) :
  character_unicode = ord(character)
  if (97 <= character_unicode <= 122):
    return character_unicode - 87
  return character_unicode - 29

print(solution(14, '9', 'd', ['9', 'a', 'c', 'd', 'e'])) # 3
print(solution(62, 'Z', '12', ['Z', '10', '11', '12'])) # 0
