pos= -1
def binarysearch(list1,n):
    l=0
    u=len(list1)-1
    while l <=u:
        mid= (l+u)//2
        if list1[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1;
            else:
                u=mid-1;
list1=[10,11,12,13,14,15]
n=15
if binarysearch(list1,n):
    print("found at",pos+1)
else:
    print("not found")
            
