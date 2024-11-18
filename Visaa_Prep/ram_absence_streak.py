N=int(input())
attend=list(map(int,input().split()))
max_no_of_absentees=0
current_absentees=0
for i in attend:
    if i==0:
        current_absentees+=1
    else:
        max_no_of_absentees=max(max_no_of_absentees,current_absentees)
        current_absentees=0
max_no_of_absentees=max(max_no_of_absentees,current_absentees)
print(max_no_of_absentees)
