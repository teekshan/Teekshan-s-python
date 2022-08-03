# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num=153
sum=0
temp=num
while temp>0:
    digit=num%10
    sum += digit**3
    temp //=10
    
if num == sum:
    print(num, "is armstrong")
else:
    print("not")
