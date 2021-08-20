import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):

    N = int(input())//10
    box = [1]
    for i in range(1, N+1):
        if i%2:                 # N을 10으로 나눈게 홀수면
            box.append(box[i-1]*2 -1)
        else:                   # 짝수인 경우
            box.append(box[i-1]*2 +1)
    print('#{} {}'.format(tc, box[-1]))
