def common_prefix():
    list2=[]
    for i in zip(*b):
        if (i.count(i[0])==len(i)): 
            list2.append(i[0])
        else:
            break
    print(''.join(list2))
a=int(input())
b=[]
for i in range(0,a):  
    u=input()
    b.append(u)
common_prefix()
