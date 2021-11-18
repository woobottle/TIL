import re

def calc(array) :
  answer = int(array[0])
  if array[1] == 'D' :
    answer = answer ** 2
  elif array[1] == 'T' :
    answer = answer ** 3
  return answer

def solution(dartResult):
  answer = 0
  results = re.findall('[0-9][0-9]?[S|D|T]+[*|#]?', dartResult)

  l = []

  for result in results:
    l.append(list(filter(lambda x : x != '', re.split('(\D)', result))))
  
  result = []

  for i in l :
    result.append(calc(i[:2]))  

  options = []
  for i in l :
    if len(i) == 3 :
      options.append(i[2])
    else :
      options.append('')

  ops = []
  
  for i in range(len(options)) :
    if options[i] == '#' :
      pass
    elif options[i] == '*' : 
      pass
  return answer

print(solution("1S2D*3T"))	# 37
# print(solution("1D2S10S"))  # 9
# print(solution("1D2S0T"))  # 3
# print(solution("1S*2T*3S"))	# 23	
# print(solution("1D2S*3S"))  # 5
# print(solution("1T2D3D"))  # -4
# print(solution("1D2S3T*"))  # 59
