def perimeter(N,stick):
    stick.sort()
    for i in range(N-1,1,-1):
        if stick[i-2]+stick[i-1]>stick[i]:
            return stick[i-2]+stick[i-1]+stick[i]
        return -1
N=int(input())
stick=list(map(int,input().split()))
print(perimeter(N,stick))
