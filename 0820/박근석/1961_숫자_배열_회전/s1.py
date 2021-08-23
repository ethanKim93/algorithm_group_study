import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
   N = int(input())
   board = []

   for i in range(N):
      board.append(input().split(' '))

   print('#{}'.format(tc))
   for i in range(N):
      for j in range(N):
         print(board[N-j-1][i], end='')
      print(end=' ')

      for j in range(N):
         print(board[N-i-1][N-j-1], end='')
      print(end=' ')

      for j in range(N):
         print(board[j][N-i-1], end='')
      print()