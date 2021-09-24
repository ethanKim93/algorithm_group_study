import sys

sys.stdin = open('sample_input.txt')


def heap_sort():                        # 이진 최소힙 트리로 정렬
    while len(nodes):                   # 입력받은 모든 노드를 순회
        heap.append(nodes.pop(0))       # heap에 node 추가
        node = heap.index(heap[-1])     # 추가된 노드의 인덱스
        parent = node // 2              # 추가된 노드의 부모 노드의 인덱스
        while True:
            if heap[node] < heap[parent]:  # 부모 노드가 새로 추가된 노드보다 크다면 자리 교체
                heap[node], heap[parent] = heap[parent], heap[node]
                node = parent           # 노드의 인덱스를 부모의 인덱스로 변경(root까지의 비교를 위해)
                parent = node // 2      # 추가된 노드의 부모 노드의 인덱스
            else:
                break

def parents_sum(n):                     # 조상 노드들의 합
    result = 0
    while n:                            # root에 도달할때까지(n==1) 부모노드의 값을 더한다
        n //= 2
        result += heap[n]
    return result

for tc in range(1, int(input()) + 1):
    N = int(input())
    nodes = list(map(int, input().split()))
    heap = [0, nodes.pop(0)]  # 1번 인덱스를 root로 heap 초기화
    heap_sort()
    answer = parents_sum(len(heap) - 1)

    print('#{} {}'.format(tc, answer))
