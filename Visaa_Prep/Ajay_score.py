T=int(input())
for _ in range(T):
    X,N=map(int,input().split())
    each_case=X//10
    score=each_case*N
    print(score)
