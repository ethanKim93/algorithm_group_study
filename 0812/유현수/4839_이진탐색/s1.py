import sys
sys.stdin=open('sample_input.txt')

def cnt(pages, key):
    result = 0
    start = 1
    end = pages
    while start <= end:
        result += 1
        middle = (start + end) // 2
        if middle == key:
            return result
        elif middle > key:
            end = middle
        else:
            start = middle

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    print(cnt(P, Pa))
    print(cnt(P, Pb))

    if cnt(P, Pa) < cnt(P, Pb):
        print('#{} A'.format(tc))
    elif cnt(P, Pa) > cnt(P, Pb):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))