n=10
def twoarr(list1):
    for i in range(len(list1)+1):
        for j in range(i):
            if list1[j]==n:
                return True
            else:
                continue
list1=[10,9,8,7,6,15,18,28,28,10]
if twoarr(list1):
    print("found at",list1.index(n)+1)
else:
    print("not found")
