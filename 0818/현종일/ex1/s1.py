
S = [0] *10
top = -1

def push(S, N):
    global top
    top += 1
    S[top] = N

def pop(S):
    global top
    top -= 1
    return S[top+1]

push(S, 5)
print(pop(S))