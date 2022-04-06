INF = 1e6
import sys
input = sys.stdin.readline

def BOJ1700() :
  N, K = map(int, input().split())
  arr = list(map(int, input().split()))
  count = 0

  plugins = []
  
  for i in range(K) :
    if arr[i] in plugins:
      continue

    if len(plugins) < N :
      plugins.append(arr[i])
      continue
    
    after_use_index = []
    remains = arr[i:]
    
    for j in range(N) :
      if plugins[j] not in remains :
        after_use_index.append(101)
        continue

      after_use_index.append(remains.index(plugins[j]))

    plug_out_index = after_use_index.index(max(after_use_index))
    del plugins[plug_out_index]
    plugins.append(arr[i])
    count += 1

  print(count)

BOJ1700()
