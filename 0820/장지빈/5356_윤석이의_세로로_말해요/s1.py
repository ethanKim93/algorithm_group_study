import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(T):
    arr = [input() for _ in range(5)]
    new_arr = []
    for i in range(100):
        for j in range(100):
            try:
                new_arr.append(arr[j][i])
            except:
                pass
    print('#{}'.format(tc+1), ''.join(new_arr))