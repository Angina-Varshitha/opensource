def rotate_arr(arr,k):
    N=len(arr)
    k=k%N
    rotated_arr=arr[-k:]+arr[:-k]
    return rotated_arr
N=int(input())
arr=list(map(int,input().split()))
k=int(input())
res=rotate_arr(arr,k)
print(*res)
