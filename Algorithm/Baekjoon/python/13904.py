def BOJ13904() :
  n = int(input())
  answer = [0] * 10000
  l = []
  for _ in range(n) :
    l.append(list(map(int, input().split())))
  l.sort(key= lambda x : (-x[1]))
  print(l)
  for i in range(n) :
    for j in range(l[i][0] -1, -1, -1) : # 그 날부터 거꾸로 가면서 비어있는칸에 넣어버리자!!
      if answer[j] == 0 : # 마감일보다 전의 날중에 0인 날이 있다면 값을 넣어 주면 됨
        answer[j] = l[i][1]
        break
  print(sum(answer))
BOJ13904()

# https://blog.naver.com/PostView.naver?blogId=namucoding_pohang&logNo=222367789087&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
