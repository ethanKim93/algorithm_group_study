import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    stack = [0, 1, 3]

    if N == 10:  # N이 10일 경우 값 1
        result = stack[1]
    elif N == 20:  # N이 20일 경우 값 3
        result = stack[2]
    else:
        for _ in range(3, N//10 + 1):
            stack.append(stack[-2]*2 + stack[-1])  # (N-2일때 경우의 수) * 2 + (N-1일때 경우의 수) = N일때 경우의 수
            result = stack[-1]


    print('#{} {}'.format(test_case, result))

