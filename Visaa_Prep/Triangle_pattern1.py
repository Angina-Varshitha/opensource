N=int(input())
n=1
for i in range(1,N+1):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()
