import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
   board = [['@']*15 for i in range(5)]
   word = ''

   for i in range(5):
      k = input()
      for j in range(len(k)):
         board[i][j] = k[j]

   for i in range(15):
      for j in range(5):
         if board[j][i] != '@':
            word += board[j][i]

   print('#{} {}'.format(tc, word))