import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    wish_pair = list(map(int, input().split()))
    pair = [[] for _ in range(N+1)]
    matched_one = [0] * (N+1)
    result = 0

    for i in range(len(wish_pair)//2):
        pair[wish_pair[i*2]].append(wish_pair[i*2+1])
        pair[wish_pair[i*2+1]].append(wish_pair[i*2])

    stack = []
    i = 1
    while i <= N:
        flag = False
        stack.append(i)
        i += 1
        while stack:
            v = stack.pop()
            requested = pair[v]

            if not requested:
                flag = True
                break

            for req in requested:
                if not matched_one[req]:
                    flag = True
                    matched_one[req] = 1
                    stack.append(req)
        if flag:
            result += 1

    print("#{} {}".format(tc, result))





