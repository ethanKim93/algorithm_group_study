import sys
sys.stdin = open('sample_input.txt')

def inorder_traverse(val): # 중위순회 식으로 tree 만들기
    global ind # 채워넣는 숫자
    if val <= N: # 새롭게 형성된 노드 번호가 최대 노드 번호 이하일 때
        inorder_traverse(2*val) # 왼쪽 서브트리로 이동
        ind += 1
        tree[val] = ind
        inorder_traverse(2*val+1) # 오른쪽 서브트리로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    ind = 0
    inorder_traverse(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))