import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def preorder(node):
  global cnt
  if node == 0:
    return
  cnt+=1
  preorder(left[node])
  preorder(right[node])

for tc in range(1, T+1) :
  E, N = map(int, input().split())
  arr = list(map(int, input().split()))
  left = [0]*(E+2)
  right = [0]*(E+2)

  for i in range(0, len(arr), 2):
    a, b = arr[i], arr[i+1]
    if left[a]:
      right[a] = b
    else:
      left[a] = b

  cnt=0
  preorder(N)
  print('#{} {}'.format(tc, cnt))