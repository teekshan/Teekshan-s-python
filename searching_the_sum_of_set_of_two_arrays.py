a=[1,2,3,7,8]
b=[2,5,6,8,9]
t=9
c=[]
for i in range(len(a)): #if you know python then reduce its complexity that is the number fo loops
    for j in b: #foise loop
    
        result=a[i]+j
        
        c.append(result)
for idx,i in enumerate(c):
    if t==i:
        print("found at ",idx+1)
        break
    continue
print(c)

