import sys
sys.stdin = open("sample_input.txt")


dr = [1,-1,0,0]
dc = [0,0,1,-1]

T = int(input())


for tc in range(1,T+1):
  N = int(input())
  board = [list(map(int,input().split())) for _ in range(N)]
  visit = [0]*(N*N)

  for i in range(N):
      for j in range(N):
          for k in range(4):
              nr = dr[k] + i
              nc = dc[k] + j

              if 0<= nr < N and 0 <= nc <N  and board[i][j] == board[nr][nc] - 1:
                  visit[board[i][j]] = 1

  max_cnt = 1
  max_idx = 1
  cnt = 1
  for idx,c in enumerate(visit):
      if c:
        cnt += 1
      else:
         if max_cnt < cnt:
            max_cnt = cnt
            max_idx = idx-cnt+1
         cnt = 1
  if max_cnt < cnt:
      max_cnt = cnt
      max_idx = idx - cnt + 1
  if max_idx == 0:
      max_idx +=1


  print('#{} {} {}'.format(tc,max_idx,max_cnt))