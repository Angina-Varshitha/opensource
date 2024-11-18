N=int(input())
arr=list(map(int,input().split()))
ele=[]
for num in arr:
    if num not in ele:
        ele.append(num)
print(" ".join(map(str,ele)))
