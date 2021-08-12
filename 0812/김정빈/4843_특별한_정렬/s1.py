import sys
sys.stdin = open("sample_input.txt")

def selection(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

#정렬 후 출력 양끝을 번갈아가면서 하기
#양끝 팝한담음에 new에 순서대로 어펜드
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    selection(ai)

    new = []
    n = len(ai)
    while n > 0:
        new.append(ai.pop(-1))
        new.append(ai.pop(0))
        n-=2
        if len(new) == 10:
            break

    print('#{} {}'.format(tc, " ".join(map(str,new))))