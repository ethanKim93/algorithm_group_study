import sys
sys.stdin =open('input.txt')

def order1(n):      #전위
    if n:           #유효한 정점이면
        print(n, end=' ')
        order1(left[n])        #n 의 왼쪽 자식으로 이동
        order1(right[n])
def order2(n):      #중위
    if n:           #유효하고
        order2(left[n])     #n의 왼쪽 자식이 있는지 없는지 확인 / 없을때까지
        print(n, end=' ')   #방문할 자식이 었으면 리턴되고 본인 출력
        order2(right[n])    #올라가며 부모노드 반환
def order3(n):      #후위
    if n:           #유효하고
        order3(left[n])     #n의 왼쪽 자식이 있는지 없는지 확인하고
        order3(right[n])
        print(n, end=' ')   #부모노드를 제일 마지막에 반환
V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0]*(V+1)
right = [0]*(V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2 +1]
    if left[p] == 0:        #P의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c

order1(1)
print()
print('#########################')
order2(1)
print()
print('#########################')
order3(1)
# 1 2 4 3 5 6