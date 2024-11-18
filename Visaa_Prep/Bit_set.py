def ck_kbit(N,X):
    bit=1<<(X-1)
    if N & bit:
        return "true"
    else:
        return "false"
N=int(input())
X=int(input())
print(ck_kbit(N,X))
