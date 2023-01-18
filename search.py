def find(list1,n):
    x=[]
    for i,value in enumerate(list1):
        if value==n:
            x.append(i+1)
    return x
list1=[1,1,1,3,4,4,4,5,6,7,10]
n=4
print(find(list1,n))
