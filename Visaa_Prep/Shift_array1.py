def rotate_arr(arr):
    return arr[1:]+arr[:1]
N=int(input())
arr=list(map(int,input().split()))
rotated_arr=rotate_arr(arr)
print(" ".join(map(str,rotated_arr)))
