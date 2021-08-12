import sys
sys.stdin = open("sample_input.txt")

#선택 정렬 정의
def selection_sort(a):
    for i in range(len(a)-1):
        amin = i
        for j in range(i+1,len(a)):
            if a[amin] > a[j]:
                amin = j
        a[i], a[amin] = a[amin], a[i]
    return a

for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    a = selection_sort(a)

    asort = []
    for i in range(10):
        if not i%2:
            asort.append(a[-i//2-1])
        else:
            asort.append(a[i//2])

    print('#{} {}'.format(tc,' '.join(map(str, asort))))




