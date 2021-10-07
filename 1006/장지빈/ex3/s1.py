import sys
sys.stdin = open('input.txt')

def order1(n):   # 전
    if n:
        print(n, end=' ')
        order1(EL[n])
        order1(ER[n])
def order2(n):   # 중
    if n:
        order1(EL[n])
        print(n, end=' ')
        order1(ER[n])
def order3(n):   # 후
    if n:
        order1(EL[n])
        order1(ER[n])
        print(n, end=' ')

V = int(input())
E = list(map(int, input().split()))
# dic로 해결
# dic = {}
# for i in range(1, len(E)//2):
#     dic[i] = 0
# for i in range(0, len(E), 2):
#     dic[E[i]] = E[i+1]

EL = [0] * (V+1)
ER = [0] * (V+1)

for i in range(0, len(E)//2, 2):
    p, c = E[i], E[i+1]
    if not EL[p]:
        EL[p] = c
    else:
        ER[p] = c
print('전위 :', end=' ')
order1(1)
print()
print('중위 :', end=' ')
order2(1)
print()
print('후위 :', end=' ')
order3(1)



