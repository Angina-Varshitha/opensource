N=int(input())
mat=[]
for _ in range(N):
    row=list(map(int,input().split()))
    mat.append(row)
for j in range(N):
    trans_row=[mat[i][j] for i in range(N)]
    print(" ".join(map(str,trans_row)))
