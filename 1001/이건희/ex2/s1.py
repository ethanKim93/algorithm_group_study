import copy
def babyjin(temps):
    temps2 = copy.deepcopy(temps)
    global ans
    run = 0
    triplet = 0
    for i in range(len(temps2)-2):
        if temps2[i] == temps2[i+1] == temps2[i+2]:
            run += 1
            temps2[i] = temps2[i+1] = temps2[i+2] = -100

    for i in range(0,len(temps2),3):
        if temps2[i] +1 == temps2[i+1] == temps2[i+2]-1:
            triplet += 1
            temps2[i] = temps2[i+1] = temps2[i+2] = -100

    if run + triplet == 2:
        ans = True
    # print(ans)
    # print('-----------------')
    return


def permutation(k):
    if k == len(alist):
        babyjin(temps)
        return

    for i in range(len(temps)):
        if temps[i] == -1:
            temps[i] = alist[k]
            permutation(k+1)
            temps[i] = -1

alist = [1,2,4,7,8,3]
temps = [-1]*len(alist)
ans = False
permutation(0)
print(ans)