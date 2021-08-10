import sys
sys.stdin = open('input.txt')

for T in range(1,11):
    N = int(input()) #덤프 횟수
    dump = list(map(int,input().split()))

    # for i in range(N):
    #     dump[dump.index(max(dump))] -= 1
    #     dump[dump.index(min(dump))] += 1
    #
    #
    # print('#{} {}'.format(T, max(dump) - min(dump)))