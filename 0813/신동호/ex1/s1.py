# reversed
A = 'algorithm'
print(''.join(reversed(A)))
#slice notation
print(A[::-1])

# swap 식으로
B = list(input())
n = len(B)
for i in range(n//2):
    B[i], B[-1-i] = B[-1-i], B[i]
print(''.join(B))

# temp라는 임시 변수 안에 저장
C = list(input())
n = len(C)
temp=''
for i in range(n//2):
    temp = C[i]
    C[i] = C[-1-i]
    C[-1-i] = temp
print(''.join(C))
