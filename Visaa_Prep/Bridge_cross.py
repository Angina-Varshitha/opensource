X,Y,Z = map(int, input().split())
if Z>=Y:
    max=(Z - Y)//X
else:
    max=0
print(max)
