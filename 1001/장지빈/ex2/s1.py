li = [[1, 2, 4, 7, 8, 3], [6, 6, 7, 7, 6, 7], [0, 5, 4, 0, 6, 0], [1, 0, 1, 1, 2, 3]]
def make(n, k, ls):
    if n == k:
        check_baby(ls)
        return
    else:
        for i in range(k, n):
            ls[k], ls[i] = ls[i], ls[k]
            make(n, k+1, ls)
            ls[k], ls[i] = ls[i], ls[k]

def check_baby(ls):
    run = triplet = 0
    if (ls[0]+1 == ls[1] and ls[1]+1 == ls[2]) or (ls[3]+1 == ls[4] and ls[3]+2 == ls[5]):
        run = 1
    if ls[0] == ls[1] == ls[2] or ls[3] == ls[4] == ls[5]:
        triplet = 1
    if run and triplet == 2:
        return check.append('2')
    elif run and not triplet:
        return check.append('1')
    elif not run and triplet:
        return check.append('0')
    return

for _ in range(len(li)):
    check = []
    make(6, 0, li[_])
    if '2' in check:
        print('#{} : baby-gin'.format(_+1))
    elif '1' in check:
        print('#{} : run'.format(_+1))
    elif '0' in check:
        print('#{} : triplet'.format(_+1))
    else:
        print('#{} : nothing'.format(_+1))
