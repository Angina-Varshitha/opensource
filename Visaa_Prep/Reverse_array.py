N=int(input().strip())
arr=list(map(int,input().strip().split()))
rev_arr=arr[::-1]
print(" ".join(map(str,rev_arr)))
