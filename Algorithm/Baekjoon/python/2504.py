import sys
input = sys.stdin.readline

def BOJ2504() :
  def is_good(args) :
    stack = []
    flag = True

    for arg in args :
      if arg == '(' :
        stack.append('(')

      if arg == ')' :
        if not stack:
          flag = False
          break

        if stack[-1] != '(' :
          flag = False
          break
        stack.pop()

      if arg == '[' :
        stack.append('[')

      if arg == ']' :
        if not stack :
          flag = False
          break

        if stack[-1] != '[':
          flag = False
          break
        stack.pop()

    if len(stack) != 0 :
      flag = False
    return flag

  def get_num(args) :
    ans = 0

    while args :
      s = args.pop()

      if s == '(' or s == '[' :
        ans += get_num(args)
      
      if s == ')' :
        return 2 * max(1, ans)

      if s == ']' :
        return 3 * max(1, ans)

    return ans

  
  s = list(input().strip())
  
  if(is_good(s)) :  
    result = get_num(s[::-1])
    print(result)
    return

  print(0)
  return


BOJ2504()
