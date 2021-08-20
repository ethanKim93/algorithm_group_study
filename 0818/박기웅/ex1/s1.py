import sys
sys.stdin = open("input.txt") # in 2, 3, 4

n = 3 # 3개의 데이터가 주어진다고 가정
stack = [0]*n
top = -1
# push
for _ in range(n):
    top += 1
    stack[top] = input()
# pop
for _ in range(n):
    top -= 1
    print(stack[top+1])
    stack[top+1] = 0 # 초기화 해줌

print(stack)



