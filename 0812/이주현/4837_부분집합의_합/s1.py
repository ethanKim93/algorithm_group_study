import sys
sys.stdin = open('sample_input.txt')

def bit_count(number, length):           # 1인 비트 수 반환
    count = 0
    for i in range(length):
        if number & (1 << i):
            count += 1
    return count

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0

    for i in range(1 << len(A)):                # 경우의 수만큼
        if bit_count(i, len(A)) == N:           # 1인 비트수가 N개일 때 -> 원소가 N개인 부분집합
            tmp = 0
            for j in range(len(A) + 1):
                if i & (1 << j):
                    tmp += A[j]
            if tmp == K:
                count += 1

    print("#{} {}".format(test_case, count))