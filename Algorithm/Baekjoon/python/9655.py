import sys
from collections import deque
input = sys.stdin.readline

def BOJ9655() :
  N = int(input())
  players = ["SK", "CY"]
  dp = [3 for _ in range(1001)]
  dp[0] = 1

  for i in range(1001) :
    if dp[i] != 3 :
      player = dp[i]
      next_player = player ^ 1
      if i + 1 < 1001 :
        dp[i+1] = next_player
      if i + 3 < 1001:
        dp[i+3] = next_player

  print(players[dp[N]])
BOJ9655()


# https://js1jj2sk3.tistory.com/30
