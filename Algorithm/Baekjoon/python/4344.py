import math
import sys
input = sys.stdin.readline

def BOJ4344() :
  C = int(input())
  for _ in range(C) :
    inputs = list(map(int, input().split()))
    total = inputs[0]
    scores = inputs[1:]
    standard = sum(scores) / total
    over_standard_scores = list(filter(lambda x: float(x) > standard, scores))
    # result = math.floor(((len(over_standard_scores) / total * 100) + 0.0005) * 1000) / 1000
    result = round((len(over_standard_scores) / total) * 100, 3)
    
    
# BOJ4344()

# https://ming-jee.tistory.com/124

# result = 40.0
# print(("%.3f" % result) + "%") # 40.000%
# print("{}%".format(result)) # 40.0%
# print("{:.3f}%".format(result))  # 40.000%
# print("{0:.3f}%".format(result))  # 40.000%
# print("{0:7.2f}% ".format(result))  #  40.00%
# print("{0:07.2f}% ".format(result))  # 0040.00%
# print("{0:07.3f}% ".format(result))  # 040.000%
# print("{0:07.4f}% ".format(result))  # 40.0000%
# print("{0:07.5f}% ".format(result))  # 40.00000%
# print("{0:08.3f}%".format(result))  # 0040.000%
# print("{0:010.3f}%".format(result))  # 000040.000%
# # "{자릿수:전체자릿수:소수점 이하 자릿수}"
# # 전체자릿수에는 . 포함 7자리면 40.0000
# # 0을 입력해주지 않으면 빈자리로 채워줌

# print("{0}% {1}%".format('a', 'b')) # a% b%
# print("{1}% {0}%".format('a', 'b')) # b% a%


print("{}".format(round(3.141592, 4)))
# 0040.00%
# 040.000%

