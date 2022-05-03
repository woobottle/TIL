# def solution(s):
#     answer = 0
#     hash_list = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
#     filtered = list(filter(lambda x : x != '',re.split('(\d)', s)))
#     answer = []
#     for i in filtered :
#         if len(i) >= 6 :
#             temp_str = i
#             index = 3
#             while len(temp_str) != 0 :
#                 if temp_str[:index] in hash_list:
#                     answer.append(str(hash_list[temp_str[:index]]))
#                     temp_str = temp_str[index:]
#                     index = 3
#                 else :
#                     index += 1

#         elif len(i) >= 3 :
#             answer.append(str(hash_list[i]))
#         else :
#             answer.append(i)
#     return ''.join(answer)


def solution(s):
    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key, value in num_dic.items():
        s = s.replace(key, value)
    return int(s)


print(solution("one4seveneight")) # 1478
print(solution("23four5six7"))	# 234567
print(solution("2three45sixseven"))	# 234567
print(solution("123"))	# 123
