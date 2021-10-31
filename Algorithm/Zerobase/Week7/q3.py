def solution(s1, s2, s3) :  
  def possible_check(s1, s2, s3) :
    s1_list, s2_list, s3_list = list(s1), list(s2), list(s3)
    for i in list(s3) :
      if(len(s1_list) and len(s2_list) and i == s1_list[0] and i == s2_list[0]) :
        return possible_check(s1[1:], s2[:], s3[1:]) or possible_check(s1[:], s2[1:], s3[1:])
      elif(len(s1_list) and i == s1_list[0]) :
        return possible_check(s1[1:], s2[:], s3[1:])
      elif(len(s2_list) and i == s2_list[0]) :
        return possible_check(s1[:], s2[1:], s3[1:])
      else:
        return False
    return True
  return possible_check(s1, s2, s3)


print(solution("aabcc", "dbbca", "aadbbcbcac")) # True
print(solution("aabcc", "dbbca", "aadbbbaccc")) # False