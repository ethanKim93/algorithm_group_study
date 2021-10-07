import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
left = (N+2)*[0]
right = (N+2)*[0]

def preorder(node):
  global cnt
  if node == 0:
    return
  cnt+=1
  preorder(left[node])
  preorder(right[node])

for i in range(0, len(arr), 2):
    a = arr[i]
    b = arr[i+1]
    if left[a]:
      right[a] = b
    else:
      left[a] = b

preorder()