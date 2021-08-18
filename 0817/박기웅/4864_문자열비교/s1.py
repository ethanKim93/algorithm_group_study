import sys
sys.stdin = open("sample_input.txt")
for tc in range(1, int(input())+1):
    fst = input()
    scd = input()
    fst_n = len(fst)
    scd_n = len(scd)
    ans = 0
    for i in range(scd_n-fst_n+1):
        if scd[i:i+fst_n] == fst:
            ans = 1
            break

    print('#{} {}'.format(tc, ans))