#p[] : 데이터가 저장된 배열
#n : 원소의 개수, i : 선택된 원소의 수

def perm(n, k):
    if k == n:
        print(p)
        return

    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]

p = [1, 2, 3]
perm(3, 0)