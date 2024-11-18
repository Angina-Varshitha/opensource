def rev_int(N):
    is_neg=N<0
    rev_num=int(str(abs(N))[::-1])
    if is_neg:
        rev_num=rev_num
    if rev_num < -2**31 or rev_num > 2**31-1:
        return 0
    return rev_num
N=int(input())
print(rev_int(N))
