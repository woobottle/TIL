def solution(words, queries):
  answer = []

  for query in queries : 
    count = 0
    is_start_head = False
    start_index = list(query).index("?")
    replaced_query = query.replace("?", "")
    last_index = 0

    if start_index == 0 :
      is_start_head = True
      last_index = len(query) - 1 - start_index
    
    for word in words :
      splitted_word = word[:start_index]
      if is_start_head :
        splitted_word = word[last_index:]

      if replaced_query == splitted_word and len(query) == len(word) :
        count += 1
    answer.append(count)
  return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries)) # [3, 2, 4, 1, 0]
