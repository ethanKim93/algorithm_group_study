# 전위 순회
def pre_order(v):
    if v:
        print(v, end = ' ')
        pre_order(left[v])
        pre_order(right[v])
def in_order(v):
    if v:
        in_order(left[v])
        print(v, end = ' ')
        in_order(right[v])
def post_order(v):
    if v:
        post_order(left[v])
        post_order(right[v])
        print(v,end = ' ')

V = int(input())
edge = list(map(int,input().split()))
E = V-1
left = [0]*(V+1)    # 왼쪽과 오른쪽 공간을 만들어줌
right = [0]*(V+1)

for i in range(E): # 인접리스트 생성
    p,c = edge[i*2],edge[i*2+1]
    if left[p]==0: # p의 왼쪽자식이 없으면
        left[p] = c
    else:          # p의 왼쪽자식이 있으면 오른쪽 자식으로 저장
        right[p] = c
pre_order(1)
print()
in_order(1)
print()
post_order(1)