import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    result = 0
    while trucks:
        for i in range(len(containers)):
            if trucks[0] >= containers[i]:
                result += containers.pop(i)
                trucks.pop(0)
                break
        else:
            break

    print('#{} {}'.format(tc, result))


