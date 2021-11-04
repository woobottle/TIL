def solution(N):
  ameba = [1, 2]
  for i in range(2, N+1) :
    ameba.append(ameba[i-2] + ameba[i-1])

  time = [0] * (N + 1) 
  for i in range(N + 1) :
    if i == 0 :
      time[i] = 1
    elif i == 1 :
      time[i] = 2
    else :
      time[i] = 2 * (ameba[i] - ameba[i-1])

  return sum(time)

print(solution(2))
print(solution(4))

