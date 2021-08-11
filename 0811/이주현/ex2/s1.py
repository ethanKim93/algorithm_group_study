import sys
sys.stdin = open('input.txt')

def summury(tmp):
    result = 0
    for idx in range(len(tmp)):
        result += tmp[idx]

    return result

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1 << len(arr)):
        tmp = 1
        part = []
        for j in range(len(arr)+1):
            if i & (1 << j):
                part += [arr[j]]

        #공집합의 경우 제외
        if len(part):
            tmp = summury(part)
        if not tmp:
            result = 1
    print(result)

