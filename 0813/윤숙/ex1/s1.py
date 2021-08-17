s = 'Reverse this strings'

# 1. slice() 사용

# print(s[::-1])


# 2. reverse() 사용

# List_S=[]
# for j in s:
#     List_S.append(j)
#
# List_S.reverse()
#
# result=','.join(List_S)
#
# print(result)


# 3. List를 이용한 방법
List_S=[]
for j in s:
    List_S.append(j)

N=len(List_S)
N=N-1
idx=int(len(List_S)/2)
                #10까지

for i in range(0,idx,1):
    tmpA=List_S[i] #0 #1
    tmpB=List_S[N-i] #9 #8
    List_S[i]=tmpB
    List_S[N-i]=tmpA

result=''.join(List_S)

print(result)
