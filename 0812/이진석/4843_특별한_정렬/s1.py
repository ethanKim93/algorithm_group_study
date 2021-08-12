import sys

sys.stdin = open('sample_input.txt')


def zigzag_search(arr, idx):
    temp = arr[0]   # 최대 or 최소값 담을변수
    temp_idx = 0    # temp의 idx를 담을 변수
    if idx % 2:  # 홀수번째 인덱스일경우 배열의 최댓값
        for k in range(len(arr)):
            if temp > arr[k]:
                temp = arr[k]
                temp_idx = k
    else:  # 짝수번째 인덱스일경우 배열의 최솟값
        for k in range(len(arr)):
            if temp < arr[k]:
                temp = arr[k]
                temp_idx = k
    return arr.pop(temp_idx)  # 최소 or 최대값의 인덱스를 배열에서 pop 하면서 value 리턴.


for tc in range(1, int(input()) + 1):
    N = int(input())
    result = []
    numbers = list(map(int, input().split()))
    i = 0
    while i < 10:  # 10개의 숫자만 출력하기 위해 반복문 10회
        result.append(zigzag_search(numbers, i))
        i += 1
    answer = ' '.join(map(str, result))
    print('#{} {}'.format(tc, answer))
