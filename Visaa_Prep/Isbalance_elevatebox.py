def bal_arr(N,A):
    B=[]
    for i in range(N):
        lw=sum(A[:i])
        rw=sum(A[i+1:])
        B.append(abs(lw-rw))
    return B
N=int(input())
A=list(map(int,input().split()))
B=bal_arr(N,A)
print(" ".join(map(str,B)))
