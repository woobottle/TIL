n = int(input())

array = {}
for i in range(n) :
  array[int(input())] = i

sorted_array = {}
temp_sorted_array = sorted(array)
for i in range(len(temp_sorted_array)) :
  sorted_array[temp_sorted_array[i]] = i

answer = 0
for i in array :
  answer = max(sorted_array[i] - array[i] + 1, answer)  

print(answer)

# 정렬이 될때마다 숫자가 왼쪽으로 이동한다. 제일 많이 이동한 번호를 찾으면 그게 정답