import sys
sys.stdin = open('input.txt')

def pre_order(n):               # 전위순회
    if n:
        print(n,end=' ')
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):                # 중위순회
    if n:
        in_order(left[n])
        print(n,end=' ')
        in_order(right[n])
        
def post_order(n):              # 후위순회
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n,end=' ')


V = int(input())    # 노드의 갯수
edges = list(map(int, input().split())) # 연결된 정점 입력
left = [0] * (V+1)  # 부모를 인덱스로 자식 번호 저장
right = [0] * (V+1)

for i in range(V-1):
    P, C = edges[i*2], edges[i*2+1]
    if left[P] == 0:
        left[P] = C
    else:
        right[P] = C
pre_order(1)
print('# 전위 순회')
in_order(1)
print('# 중위 순회')
post_order(1)
print('# 후위 순회')
