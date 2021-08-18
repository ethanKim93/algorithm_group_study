#풀이_1
# s = []
# s.append(1)
# s.append(2)
# s.append(3)
# print(s)
# print(s.pop(2))
# print(s.pop(1))
# print(s.pop(0))
# print(s)

#풀이 2
top = -1
S = []

def push(i):
    S.append(i)
def pop():
    if len(S) == 0:
        return
    else:
        return S.pop(-1)

push(1)
push(2)
push(3)
print(S)
pop()
pop()
print(S)
