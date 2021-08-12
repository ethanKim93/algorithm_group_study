import sys
sys.stdin = open("sample_input.txt")


# 선택 정렬을 오름차순, 내림차순으로 분리하여 함수로 선언한다
# 리스트는 mutable하다는 특성을 사용하여 따로 return을 하지 않는다.
def max_swap(num_lists, start_idx):
    maxIdx = start_idx
    maxV = num_lists[start_idx]
    for idx in range(start_idx + 1, len(num_lists)):
        if num_lists[idx] > maxV:
            maxIdx = idx
            maxV = num_lists[idx]
    num_lists[start_idx], num_lists[maxIdx] = num_lists[maxIdx], num_lists[start_idx]

def min_swap(num_lists, start_idx):
    minIdx = start_idx
    minV = num_lists[start_idx]
    for idx in range(start_idx + 1, len(num_lists)):
        if num_lists[idx] < minV:
            minIdx = idx
            minV = num_lists[idx]
    num_lists[start_idx], num_lists[minIdx] = num_lists[minIdx], num_lists[start_idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lists = list(map(int, input().split()))

    # 10개의 원소에 대해 특별한 정렬을 진행한다.
    for idx in range(10):
        if idx % 2:
            min_swap(num_lists, idx)
        else:
            max_swap(num_lists, idx)

    # 전체 리스트를 10개로 줄여준다.
    num_lists = num_lists[0:10]
    print("#{} {}".format(tc, " ".join(map(str, num_lists))))