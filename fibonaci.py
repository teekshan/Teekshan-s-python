# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num=int(input(""))
count=0
n1,n2=0,1
if num<=0:
    print("add positive number")
if num==1:
    print(n1)
else:
    while count<num:
        print(n1)

        nth=n1+n2
        n1=n2
        n2=nth
        count +=1
