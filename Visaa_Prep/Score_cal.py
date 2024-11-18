def score_cal(x,n):
    testcase_point=x//10
    return testcase_point*n
T=int(input())
for _ in range(T):
    X,N=map(int,input().split())
    print(score_cal(X,N))
