def ele(mat,N):
    res=[]
    for i in range(N):
        r_sum=sum(mat[i])
        c_sum=sum(mat[j][i] for j in range(N))
        res.append(r_sum+c_sum)
    return res
N=int(input().strip())
mat=[list(map(int,input().split())) for _ in range(N)]
res=ele(mat,N)
print(' '.join(map(str,res)))
