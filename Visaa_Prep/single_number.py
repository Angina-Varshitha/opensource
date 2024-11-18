def single(arr):
    res=0
    for n in arr:
        res^=n
    return res
N=int(input())
arr=list(map(int,input().split()))
print(single(arr))
