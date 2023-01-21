a=[1,2,3,7,8]
b=[2,5,6,8,9]
t=9
c=[]
for i in range(len(a)):
    for j in b:
        result=a[i]+j
        
        c.append(result)
    if t in c:
        print("found t at", len(c)-1)
        break
    else:
        continue
    
    
print(c)
