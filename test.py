# from re import A
# import sys 
# input = sys.stdin.readline

# def solve(a, b) :
#   def func(turn, a, b) :
#     if a == 0 and b == 0 :
#       if turn == 0 :
#         pass
#       if turn == 1 :
#         pass

#   dp = [[-1, -1] for _ in range(101)]
  
#   func(0, a, b)
  

#   print(dp[a][b])

    
# solve(0, 100) # 0, 1
# solve(1, 2) # 1, 2
# solve(1, 4) 
# solve(3, 1) 
# solve(97, 4) 
# solve(2, 3) 
# solve(2, 4) 
# solve(3, 5) 
# solve(5, 3) 

# # 내가 생각한 가장 빨리 이기는 법 -> 숫자 둘중 하나를 1로 만들어 버리자
# # 내가 생각한 가장 느리게 지는 법 -> 1개만 빼기

a = [1, 2, 3]
b = [100, 200, 300]
c = [4, 5, 6]

for i, j, k in zip(a, b, c) :
  print(i, j, k)

print(*a)
print(*b)