# def toggle_item(x) :
#   if x == '1' :
#     return '0'
#   return '1'

# def toggle(s, i) :
#   s = list(s)
  
#   if i == 0 :
#     s[:2] = list(map(toggle_item, s[:2]))
#   elif i == len(s) :
#     s[i-2:] = list(map(toggle_item, s[i-2:]))
#   else :
#     s[i-1:i+2] = list(map(toggle_item, s[i-1:i+2]))
#   return ''.join(s) 

# n = input()
# first = input()
# second = input()

# # bfs
# bfs = []
# result_list = {}
# result_list[first] = 0
# bfs.append([first, 0])

# while True :
#   if len(bfs) == 0:
#     break
  
#   target, count = bfs.pop(0)
  
#   if target == second :
#     break
#   for i in range(len(target)) :
#     toggle_target = toggle(target, i)
#     if toggle_target in result_list :
#       result_list[toggle_target] = min(result_list[toggle_target], count+1)
#     else :
#       result_list[toggle_target] = count+1
#     bfs.append([toggle_target, count+1])

# if second in result_list :
#   print(result_list[second])
# else :
#   print(-1)


# 첫번째 전구를 바꾸는 경우와 바꾸지 않는 경우로 나누자

n = input()
first = list(input())
target = list(input())

def change_zero_index(light) :
  count = 1
  light[0] = str(1 - int(light[0]))
  light[1] = str(1 - int(light[1]))

  for i in range(1, len(light)) :
    if target[i-1] != light[i-1] :
      count += 1
      light[i-1] = str(1 - int(light[i-1]))
      light[i] = str(1 - int(light[i]))
      if i != int(n) - 1 :
        light[i+1] = str(1 - int(light[i+1]))

  if light == target:
      return count

  
  return 100001

def not_change_zero_index(light) :
  count = 0
  
  for i in range(1, len(light)):
    if target[i-1] != light[i-1]:
      count += 1
      light[i-1] = str(1 - int(light[i-1]))
      light[i] = str(1 - int(light[i]))

      if i != int(n) - 1:
        light[i+1] = str(1 - int(light[i+1]))

  if light == target:
      return count 

  return 100001

answer_first = change_zero_index(first[:])
answer_second = not_change_zero_index(first[:])
answer = min(answer_first, answer_second)

if answer == 100001 :
  print(-1)
else :
  print(answer)
