x2=int(input())
y2=list(map(int,input().split()))
z3=[]
for x in range(x1):
    for i in range(x+1,len(y2)):
        if(y2[i]==y2[x]):
          z3.append(y2[x])
if (len(z3)==0):
    print("unique")
else:
    z3.sort()
    li2=set(z3)
    for x in li2:
        print(x,end=" ")
