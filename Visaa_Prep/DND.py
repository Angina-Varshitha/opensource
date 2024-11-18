def cal_diff(arr,M):
    n1=sum(x for x in arr if x %M != 0)
    n2=sum(x for x in arr if x%M == 0)
    return n2-n1
N,M=map(int,input().split())
arr=list(map(int,input().split()))
print(cal_diff(arr,M))
