T = 12
inputV = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# 완전 이진 트리 아님

arr = list(map(int, inputV.split()))

left = [0] * 14  # 인덱스가 부모, value가 자식
right = [0] * 14

for i in range(0, len(arr), 2):
    if left[arr[i]] == 0:
        left[arr[i]] = arr[i+1]
    else:
        right[arr[i]] = arr[i+1]

# 루트 노드 찾기 / 인덱스가 자식, value가 부모
root = [0] * 14
rootIdx = 0  # 트리의 루트값
for j in range(len(left)):
    if left[j] != 0:
        root[left[j]] = j
for k in range(len(right)):
    if right[k] != 0:
        root[right[k]] = k
for l in range(1, len(root)):
    if root[l] == 0:
        rootIdx = l
        break

# 전위 순회
def preorder_traverse(node):
    if node is

