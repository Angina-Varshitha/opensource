def str_red(M):
    res=""
    count=1
    for i in range(1,len(M)):
        if M[i]==M[i-1]:
            count+=1
        else:
            res+=M[i-1]+str(count)
            count=1
    res+=M[-1]+str(count)
    return res
N=input()
print(str_red(N))
